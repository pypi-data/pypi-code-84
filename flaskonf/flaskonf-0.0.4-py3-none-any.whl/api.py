# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/10_api.ipynb (unless otherwise specified).

__all__ = ['open_json', 'open_file', 'mkdir', 'clean_up_string', 'error_printer', 'time_str', 'Directories',
           'FlaskonfAPI']

# Cell
from flask import Flask, send_file,request
from pathlib import Path
import json, os, logging
from typing import Callable, List, Dict
import traceback
from jinja2 import Template
from datetime import datetime

# Cell

def open_json(path: Path):
    with open(path, "r") as f:
        return json.loads(f.read())

def open_file(path: Path):
    with open(path, "r") as f:
        return f.read()

def mkdir(path: Path):
    path.mkdir(exist_ok=True, parents=True)

def clean_up_string(x):
    x2 = x.lower().replace("/"," ").strip().replace(" ","_")
    while "__" in x:
        x2 = x2.replace("__", "_")
    return x2

def error_printer(e: Exception):
    logging.error(traceback.format_exc())
    return dict(error_msg=str(e))

def time_str():
    return datetime.now().strftime("%y%m%d_%H%M%S")

# Cell
class Directories:
    def __init__(self):
        self.allocate()

    def allocate(self):
        self.root = self.find_root()

    def find_root(self):
        import flaskonf
        return Path(flaskonf.__file__).parent

    @property
    def static_dir(self):
        return self.root/"static"

    @property
    def templates_dir(self):
        return self.root/"templates"

    def open_templates(self, relative_temp_path):
        with open(self.templates_dir/relative_temp_path, "r") as f:
            return Template(f.read())

    def render_templates(self, template, **kwargs):
        return self.open_templates(template).render(**kwargs)

    def header_files(self):
        return [
            {"type":"script", "path": "js/jquery.min.js"},
            {"type":"script", "path": "js/bootstrap.min.js"},
            {"type":"css", "path": "css/bootstrap.css"},
        ]

    def __repr__(self):
        return f"""
        - root:{self.root}
            - static:{self.static_dir}
            - static:{self.templates_dir}
        """

    def ls_recursively(self, path):
        options = os.listdir(path)
        result = []
        for option in options:
            if (Path(path)/option).is_dir():
                result+= self.ls_recursively(Path(path)/option)
            else:
                result.append(str(Path(path)/option))
        return result

# Cell
class FlaskonfAPI(Flask, Directories):
    """
    # create an flask app
    app = FlaskonAPI("alpha_api")

    # assign address for directories full of json
    app.build_on_config(
        confs_dir="../tests/confs/",
        examples_dir="../tests/examples/"
        )

    # create an api blueprint
    # with such blueprint, we can have an api for each configuration file
    @app.conf_route("/guide/")
    def build_city_guide(conf_file: str, conf: Dict):
        logging.info(f"{conf}")
        def guide_api(data: Dict):
            user = data["user"]
            return {"city_data": conf, "user": user}
        return guide_api

    # run api
    app.run('0.0.0.0', port=1234)
    """
    def set_dicrectory(
        app: Flask,
        confs_dir: Path=None,
        examples_dir: Path=None
    ) -> Flask:
        if confs_dir == None:
            confs_dir =Path(app.static_folder)/"confs"
            logging.warning(
                f"configuration directory not found, set to {confs_dir}")
        else:
            confs_dir = Path(confs_dir)

        if examples_dir == None:
            examples_dir =Path(app.static_folder)/"examples"
            logging.warning(
                f"example directory not found, set to {examples_dir}")
        else:
            examples_dir = Path(examples_dir)
        app.confs_dir = confs_dir
        app.examples_dir = examples_dir


    def api_get_creater(app, route, name, data):
        def wrapper():
            data.update({"examples":app.get_examples(name)})
            return app.render_templates("get_page.html", **data)
        wrapper.__name__ = f"{name}_get"
        app.route(route, methods=["GET",])(wrapper)


    def default_build(app, f):
        def builder(conf_file, conf):
            return f
        return builder

    def conf_route(
        app,
        route,
        filter_func: Callable = None,
        nobuild = False,
    ) -> Callable:
        """
        A decorator that will create new blueprint
        """
        def decorator(f):
            app.blueprint.append(dict(
                route=route,
                build_func = f if nobuild == False else app.default_build(f),
                filter_func = filter_func,
                name = f.__name__
            ))
            return f
        return decorator


    def create_api(
        app: Flask,
        route: str,
        name: str,
        conf_file:str = None,
        conf:dict = None,
        methods=["POST"],
        error_handler=error_printer,
        get_template_data=dict()):
        """
        @app.create_api(route="/calculator/sqrt/", name="get_root")
        def get_root(data):
            num = data["input_number"]
            return dict(input_number=num, root_result=(num**.5))
        """
        def deco(f):
            def wrapper():
                """
                A wrapper with error handler
                """
                try:
                    if request.data:
                        data = json.loads(request.data)
                    else:
                        data = dict()
                    inputs = dict(
                        data = data,
                        conf_file = conf_file,
                        conf = conf
                    )
                    result = f(inputs)
                    return result, 200
                except Exception as e:
                    return error_handler(e), 500
                return result
            wrapper.__name__ = name
            app.route(route, methods=["POST"])(wrapper)
            get_template_data.update({
                "page_title":f"API {name}"
            })
            app.api_get_creater(route, f"{name}", get_template_data)
            return wrapper
        return deco


    def build_blueprint(app, blueprint):
        """
        blueprint: dict, contains the following
            - filter_func: if we want to build the API
            - build_func: the actual API function to build
            - base route: str
        """
        filter_func = blueprint["filter_func"]
        filter_func = filter_func if filter_func else lambda x,y:True
        build_func = blueprint["build_func"]
        base_route = blueprint["route"]
        api_name = clean_up_string(base_route)

        for conf_file, conf in app.all_configs.items():
            # filter if we have to build this func
            if filter_func(conf_file, conf):
                title = clean_up_string(conf_file.split(".")[0])
                target_route = str(Path(base_route)/title)+"/"
                add_route = str(Path(base_route)/title/"add_example")+"/"
                built_func = build_func(conf_file, conf)

                built_func.__name__ = f"{api_name}_{title}"
                template_data = dict(
                        target_route=target_route,
                        add_route=add_route,
                    )

                if app.show_config:
                    with open(app.confs_dir/conf_file,"r") as f:
                        template_data.update(
                            {"conf_data":f.read()})

                app.create_api(
                    target_route,
                    f"{api_name}_{title}",
                    get_template_data=template_data,
                    conf_file = conf_file,
                    conf=conf
                )(built_func)

                # api for add example
                @app.create_api(
                    add_route,
                    f"{api_name}_{title}_add_example"
                )
                def add_example_file(inputs):
                    data = inputs['data']
                    example_path = Path(f"{api_name}_{title}")/f"eg_{time_str()}.json"
                    with open(app.examples_dir/example_path, "w") as f:
                        f.write(json.dumps(data))
                    return {"example_path": str(example_path)}

                logging.info(
                    f"run config\t{conf_file} on route\t{target_route}")


    def build_header(app):
        """
        send header files from static
        htype: str, like js/ css
        """
        @app.route("/header/<htype>/<filename>", methods=["GET",])
        def open_header(htype, filename):
            file_path = app.static_dir/htype/filename
            if file_path.exists():
                return send_file(file_path)
            else:
                logging.error(f"not found: {file_path}")
                return ""

    def build_flaskonf(app):
        for blueprint in app.blueprint:
            app.build_blueprint(blueprint)

    def build_on_config(
        app: Flask,
        confs_dir: Path=None,
        examples_dir: Path=None,
        show_config: bool=True,
    ) -> Flask:
        app.allocate()
        app.show_config=show_config
        app.set_dicrectory(
            confs_dir=confs_dir,
            examples_dir=examples_dir)
        # make sure directory exists
        mkdir(app.confs_dir)
        mkdir(app.examples_dir)

        app.build_header()

        app.blueprint = []
        app.all_configs = dict(
            (i, open_json(app.confs_dir/i)) for i in os.listdir(app.confs_dir))

    def get_examples(app, example_name):
        example_dir_path = app.examples_dir/example_name
        logging.debug(f"loading examples from {example_dir_path}")
        if example_dir_path.exists():
            files = os.listdir(example_dir_path)
            files = list(filter(lambda x:".json" in x, files))
            return json.dumps(dict(zip(files,map(lambda x:open_file(example_dir_path/x),files))))
        else:
            return json.dumps(dict())