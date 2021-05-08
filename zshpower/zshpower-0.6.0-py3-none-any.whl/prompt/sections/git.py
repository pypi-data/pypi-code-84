from .lib.utils import Color


class Git:
    def __init__(self, config, icon_space=" "):
        from .lib.utils import element_spacing, symbol_ssh

        self.config = config
        self.symbol = symbol_ssh(config["git"]["symbol"], "git:")
        self.color_symbol = config["git"]["color"]["symbol"]
        self.branch_color = config["git"]["branch"]["color"]
        self.prefix_color = config["git"]["prefix"]["color"]
        self.prefix_text = element_spacing(config["git"]["prefix"]["text"])
        self.symbol_enable = config["git"]["status"]["symbols"]["enable"]
        self.icons = {
            "A": [
                f"{Color('green')}"
                f"{symbol_ssh(config['git']['status']['symbol']['added'], '')}"
                f"{Color().NONE}",
                f"{Color('green')}+{icon_space}{Color().NONE}",
            ],
            # "AM": [
            #     f"{Color('white')}"
            #     f"{symbol_ssh(config_file['git']['status']['symbol']['changed'], '')}"
            #     f"{Color().NONE}",
            #     f"{Color('white')}#{icon_space}{Color().NONE}",
            # ],
            "M": [
                f"{Color('blue')}"
                f"{symbol_ssh(config['git']['status']['symbol']['modified'], '')}"
                f"{Color().NONE}",
                f"{Color('blue')}#{icon_space}{Color().NONE}",
            ],
            "D": [
                f"{Color('red')}"
                f"{symbol_ssh(config['git']['status']['symbol']['deleted'], '')}"
                f"{Color().NONE}",
                f"{Color('red')}x{icon_space}{Color().NONE}",
            ],
            "??": [
                f"{Color('yellow')}"
                f"{symbol_ssh(config['git']['status']['symbol']['untracked'], '')}"
                f"{Color().NONE}",
                f"{Color('yellow')}?{icon_space}{Color().NONE}",
            ],
            "R": [
                f"{Color('magenta')}"
                f"{symbol_ssh(config['git']['status']['symbol']['renamed'], '')}"
                f"{Color().NONE}",
                f"{Color('magenta')}->{icon_space}{Color().NONE}",
            ],
            "UU": [
                f"{Color('red')}"
                f"{symbol_ssh(config['git']['status']['symbol']['conflicts'], '')}"
                f"{Color().NONE}",
                f"{Color('red')}!={icon_space}{Color().NONE}",
            ],
            "AH": [
                f"{Color('blue')}"
                f"{symbol_ssh(config['git']['status']['symbol']['ahead'], '')}"
                f"{Color().NONE}",
                f"{Color('blue')}^{icon_space}{Color().NONE}",
            ],
            "BH": [
                f"{Color('magenta')}"
                f"{symbol_ssh(config['git']['status']['symbol']['behind'], '')}"
                f"{Color().NONE}",
                f"{Color('magenta')}_{icon_space}{Color().NONE}",
            ],
            "DG": [
                f"{Color('yellow')}"
                f"{symbol_ssh(config['git']['status']['symbol']['diverged'], '')}"
                f"{Color().NONE}",
                f"{Color('yellow')}<->{icon_space}{Color().NONE}",
            ],
            "C": [
                f"{Color('yellow')}"
                f"{symbol_ssh(config['git']['status']['symbol']['copied'], '')}"
                f"{Color().NONE}",
                f"{Color('yellow')}**{icon_space}{Color().NONE}",
            ],
            "U": [
                f"{Color('magenta')}"
                f"{symbol_ssh(config['git']['status']['symbol']['unmerged'], '')}"
                f"{Color().NONE}",
                f"{Color('magenta')}={icon_space}{Color().NONE}",
            ],
            "CL": [
                f"{Color('green')}"
                f"{symbol_ssh(config['git']['status']['symbol']['clean'], '')}"
                f"{Color().NONE}",
                f"{Color('green')}~{icon_space}{Color().NONE}",
            ],
        }
        self.icons["UD"] = self.icons["UU"]

    def __str__(self):
        from .lib.utils import separator, git_status
        from os import getcwd, environ
        from os.path import join, isdir

        if isdir(join(getcwd(), ".git")):
            status_git = git_status(porcelain=True)
            status_git_text = git_status()
            branch_current = git_status(branch=True)
            branch_formated = (
                f"{Color(self.prefix_color)}"
                f"{self.prefix_text}{Color().NONE}"
                f"{Color(self.color_symbol)}"
                f"{self.symbol}{Color().NONE}"
                f"{Color(self.branch_color)}"
                f"{branch_current}"
                f"{Color().NONE}"
            )
            status_current = []
            if "??" in status_git:
                status_current.append("??")
            if "D" in status_git:
                status_current.append("D")
            if "R" in status_git:
                status_current.append("R")
            if "A" in status_git:
                status_current.append("A")
            # if "AM" in status_git:
            #     status_current.append("AM")
            if "M" in status_git:
                status_current.append("M")
            if "UU" in status_git:
                status_current.append("UU")
            if "U" in status_git:
                status_current.append("U")
            if "UD" in status_git:
                status_current.append("UD")
            if "C" in status_git:
                status_current.append("C")
            if "ahead" in status_git_text:
                status_current.append("AH")
            if "behind" in status_git_text:
                status_current.append("BH")
            if "diverged" in status_git_text:
                status_current.append("DG")
            if len(status_git) == 0:
                status_current.append("CL")

            # # Old: No List Comprehension
            # status_icons = []
            # for item in status_current:
            #     if "SSH_CONNECTION" not in environ:
            #         if self.symbol_enable:
            #             status_icons.append(f"{self.icons[item][0]}")
            #         else:
            #             status_icons.append(f"{self.icons[item][1]}")
            #     else:
            #         status_icons.append(f"{self.icons[item][1]}")

            status_icons = [
                self.icons[item][0]
                if self.symbol_enable
                else self.icons[item][1]
                if "SSH_CONNECTION" not in environ
                else self.icons[item][1]
                for item in status_current
            ]

            # status = f'( {" ".join(sorted(status_icons)).strip()} )'
            # if len(status_current) == 1:
            status = "".join(sorted(status_icons))

            return f"{separator(self.config)}{branch_formated} {status}"
        return ""
