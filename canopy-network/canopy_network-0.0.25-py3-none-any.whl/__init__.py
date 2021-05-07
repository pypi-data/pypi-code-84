"""A decentralized social network."""

import json
from pprint import pprint
import time

from understory import kv
from understory import sql
from understory import web
from understory.web.framework.util import tx


app = web.application("Canopy", static=__name__, year=r"\d{4}", month=r"\d{2}",
                      day=r"\d{2}", seconds=web.nb60_re + r"{,4}",
                      slug=r"[\w_-]+", topic=r".+", person=r".+", event=".+")
tmpl = web.templates(__name__)


@app.route(r"")
class Home:
    """."""

    def get(self):
        recent = self.delegate(Recent)
        return tmpl.home(recent)


@app.route(r"postjob")
class PostJob:
    """."""

    def get(self):
        web.enqueue(foobar, 3)
        return "ok"


def foobar(n):
    time.sleep(5)
    print(f"batbaz {n}")


@app.route(r"people/me")
class Me:
    """."""

    def get(self):
        try:
            me = tx.pub.read("people/me")["resource"]
        except IndexError:
            raise web.OK(tmpl.new())
        return tmpl.about(me)

    def post(self):
        profile = web.form()
        profile["urls"] = profile["urls"].splitlines()
        profile["type"] = "card"
        print(profile)
        tx.pub.update("about", profile)
        raise web.SeeOther("/about")


@app.route(r"recent")
class Recent:
    """."""

    def get(self):
        recent = tx.pub.get_entries()
        return tmpl.recent(recent)


@app.route(r"now")
class Now:
    """."""

    def get(self):
        try:
            now = tx.pub.read("now")["resource"]
        except IndexError:
            tx.pub.create("now", mood={"start": [0, 0, 0], "end": [0, 0, 0]},
                          browsing=[])
            now = tx.pub.read("now")["resource"]
        return tmpl.now(now)


@app.route(r"now/peers")
class NowPeers:
    """Firehose of peers' /now braids."""

    def subscribe(self):
        return web.multi_subscribe("alice.com/now", "bob.com/now")
        # for patch in web.multi_subscribe(*peers):
        #     yield bytes(f"proxying: {patch.decode()}", "utf-8")


@app.route(r"{year}")
class ArchiveYear:
    """Resources from given year."""

    def get(self):
        return tmpl.archive.year()


@app.route(r"{year}/{month}")
class ArchiveMonth:
    """Resources from given month."""

    def get(self):
        return tmpl.archive.month()


@app.route(r"{year}/{month}/{day}")
class ArchiveDay:
    """Resources from given day."""

    def get(self):
        return tmpl.archive.day()


@app.route(r"tracks")
class Tracks:
    """Coords."""

    def post(self):
        print()
        pprint(json.loads(web.form()))
        print()


@app.route(r"{year}/{month}/{day}/{seconds}(/{slug})?")
class Entry:
    """An individual entry."""

    def get(self):
        resource = tx.pub.read(tx.request.uri.path)["resource"]
        if resource["visibility"] == "private" and not tx.user.session:
            raise web.SeeOther(f"/auth?return_to={tx.request.uri.path}")
        return tmpl.entry(resource)


@app.route(r"chat/{topic}")
class ChatTopic:
    """A chat room for given topic."""

    def get(self):
        return tmpl.chat(self.topic)


@app.route(r"network")
class Network:
    """Your social network."""

    def get(self):
        resource = tx.pub.read(tx.request.uri.path)
        return tmpl.resource(resource)


@app.route(r"network/{person}")
class Person:
    """A person in your network."""

    def get(self):
        resource = tx.pub.read(tx.request.uri.path)
        return tmpl.resource(resource)


@app.route(r"events")
class Calendar:
    """Your event calendar."""

    def get(self):
        resource = tx.pub.read(tx.request.uri.path)
        return tmpl.resource(resource)


@app.route(r"events/{event}")
class Event:
    """An event on your calendar."""

    def get(self):
        resource = tx.pub.read(tx.request.uri.path)
        return tmpl.resource(resource)


@app.route(r"icon-editor")
class IconEditor:
    """An icon editor."""

    def get(self):
        icons = {"bookmark": (576, 512, """
            M 144,32
            C 136,32 128,40 128,48
            L 128,480
            L 288,384
            L 448,480
            L 448,48
            C 448,40 440,32 432,32
            Z""")}
        return tmpl.icon_editor(icons)


@app.route(r"initialize")
class Initialize:
    """."""

    def post(self):
        name = web.form("name").name
        uid = str(web.uri(tx.origin))
        tx.pub.create("card", nickname="me", name=name, uid=uid, url=uid)
        tx.pub.create("entry", content="Hello world!")
        passphrase = web.indieauth.add_owner()
        tx.user.session["uid"] = uid
        tx.user.session["name"] = name
        tx.host.owner = tx.pub.read(uid)["resource"]
        return tmpl.welcome(passphrase)


@app.route(r"settings")
class Settings:
    """."""

    def get(self):
        return tmpl.settings()

    def post(self):
        form = web.form("theme")
        print(form.theme)
        raise web.SeeOther("/settings")


@app.route(r"debug")
class Debug:
    """Client-side debugging."""

    def get(self):
        return "debug log"


app.mount(web.cache_app)
# TODO app.mount(web.debug_app)
app.mount(web.indieauth.client)
app.mount(web.indieauth.server)
app.mount(web.indieauth.root)
app.mount(web.micropub.server)
app.mount(web.microsub.server)
app.mount(web.webmention.receiver)
app.mount(web.websub.hub)


@app.wrap
def contextualize(handler, app):
    """Contextualize this thread based upon the host of the request."""
    host = tx.request.uri.host
    tx.app.name = host
    db = sql.db(f"{host}.db")
    db.define(signins="""initiated DATETIME NOT NULL
                             DEFAULT CURRENT_TIMESTAMP,
                         user_agent TEXT, ip TEXT""",
              credentials="""created DATETIME NOT NULL
                                 DEFAULT CURRENT_TIMESTAMP,
                             salt BLOB, scrypt_hash BLOB""",
              sessions=web.session_table_sql)
    web.add_job_tables(db)
    tx.host.db = db
    tx.host.cache = web.cache(db=db)
    tx.host.kv = kv.db(host, ":", {"jobs": "list"})
    yield


app.wrap(web.resume_session)
app.wrap(web.braidify)


@app.wrap
def template(handler, app):
    """Wrap the response in a template."""
    tx.user.is_owner = tx.user.session.get("uid") == str(web.uri(tx.origin))
    yield
    if tx.response.headers.content_type == "text/html" \
       and not tx.response.naked and "owner" in tx.host:
        tx.response.body = tmpl.template(tx.host.owner, tx.response.body)


app.wrap(web.indieauth.wrap_client, "post")
app.wrap(web.indieauth.wrap_server, "post")
app.wrap(web.micropub.wrap_server, "post")
app.wrap(web.webmention.wrap, "post")
app.wrap(web.microsub.wrap_server, "post")
app.wrap(web.websub.wrap, "post")


def finalize(handler, app):
    """Leverage the IndieWeb tools above for use during this transaction."""
    if "owner" not in tx.host and tx.request.method == "GET":
        raise web.OK(tmpl.new())
    yield


app.wrap(finalize, "post")
