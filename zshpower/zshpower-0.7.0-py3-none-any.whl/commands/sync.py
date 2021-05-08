import curses
import sys
from sqlite3 import OperationalError
from snakypy import FG
from snakypy.console import loading, printer
from zshpower.commands.lib.handle import records
from zshpower.utils.check import checking_init
from zshpower.config.base import Base


class Sync(Base):
    def __init__(self, home):
        Base.__init__(self, home)

    def run(self) -> None:
        try:
            checking_init(self.HOME)
            records("update")
            curses.initscr()
            curses.curs_set(0)
            loading(
                set_time=0.040,
                bar=False,
                header="Synchronizing versions with database ...",
                foreground=FG.QUESTION,
            )
            curses.curs_set(1)
            curses.endwin()
            printer("Done!", foreground=FG.FINISH)
        except OperationalError:
            printer(
                "The database does not exist or is corrupted.",
                foreground=FG.ERROR,
            )
            sys.exit(1)
