# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['falocalrepo']

package_data = \
{'': ['*']}

install_requires = \
['faapi>=2.19.0,<2.20.0',
 'falocalrepo-database>=4.18.1,<4.19.0',
 'falocalrepo-server>=1.10.0,<1.11.0',
 'psutil>=5.8.0,<6.0.0']

entry_points = \
{'console_scripts': ['falocalrepo = falocalrepo.__main__:main']}

setup_kwargs = {
    'name': 'falocalrepo',
    'version': '3.23.13',
    'description': "Pure Python program to download any user's gallery, scraps, favorites, and journals from FurAffinity in an easily handled database.",
    'long_description': '# FALocalRepo\n\n[![version_pypi](https://img.shields.io/pypi/v/falocalrepo?logo=pypi)](https://pypi.org/project/falocalrepo/)\n[![version_gitlab](https://img.shields.io/badge/dynamic/json?logo=gitlab&color=orange&label=gitlab&query=%24%5B%3A1%5D.name&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2Fmatteocampinoti94%252Ffalocalrepo%2Frepository%2Ftags)](https://gitlab.com/MatteoCampinoti94/FALocalRepo)\n[![version_python](https://img.shields.io/pypi/pyversions/falocalrepo?logo=Python)](https://www.python.org)\n\n[![issues_gitlab](https://img.shields.io/badge/dynamic/json?logo=gitlab&color=orange&label=issues&suffix=%20open&query=%24.length&url=https%3A%2F%2Fgitlab.com%2Fapi%2Fv4%2Fprojects%2Fmatteocampinoti94%252Ffalocalrepo%2Fissues%3Fstate%3Dopened)](https://gitlab.com/MatteoCampinoti94/FALocalRepo/issues)\n[![issues_github](https://img.shields.io/github/issues/matteocampinoti94/falocalrepo?logo=github&color=blue)](https://github.com/MatteoCampinoti94/FALocalRepo/issues)\n\n[![version_pypi](https://img.shields.io/pypi/v/faapi?logo=pypi&label=faapi)](https://pypi.org/project/faapi/)\n[![version_pypi](https://img.shields.io/pypi/v/falocalrepo-database?logo=pypi&label=falocalrepo-database)](https://pypi.org/project/falocalrepo-database/)\n[![version_pypi](https://img.shields.io/pypi/v/falocalrepo-server?logo=pypi&label=falocalrepo-server)](https://pypi.org/project/falocalrepo-server/)\n\nPure Python program to download any user\'s gallery/scraps/favorites from the FurAffinity forum in an easily handled\ndatabase.\n\n## Introduction\n\nThis program was born with the desire to provide a relatively easy-to-use method for FA users to download submissions\nthat they care about from the forum.\n\nThe data is stored into a SQLite database, and the submissions files are saved in a tiered tree structure based on their\nID\'s. Using SQLite instead of a client-server database makes the program to be extremely portable, only needing a\nworking Python 3.9+ installation to work, and allows the downloaded data to be moved and backed up by simply\nmoving/copying the database file and submission files folder.\n\nAll download operations are performed through the custom FurAffinity scraping\nlibrary [faapi](https://pypi.org/project/faapi/). To ensure proper crawling behavior the library strictly follows\nFurAffinity\'s [robots.txt](https://www.furaffinity.net/robots.txt) in regard to allowed paths and crawl delay.\nFurthermore, submission files downloads are throttled to 100 KB/s to ensure the program won\'t use too much bandwidth.\n\nThe database and file-storage functions are handled independently by\nthe [falocalrepo-database](https://pypi.org/project/falocalrepo-database/) package which performs all transactions,\nqueries, and file operations.\n\nThe [falocalrepo-server](https://pypi.org/project/falocalrepo-server/) package is used to provide the server\nfunctionalities of the program.\n\n## Contents\n\n1. [Installation and Update](#installation-and-update)\n1. [Cookies](#cookies)\n1. [Usage](#usage)\n    1. [Environmental Variables](#environmental-variables)\n    1. [Error Codes](#error-codes)\n    1. [Help](#help)\n    1. [Init](#init)\n    1. [Configuration](#configuration)\n    1. [Download](#download)\n    1. [Database](#database)\n1. [Database](#database-1)\n    1. [Settings](#settings)\n    1. [Users](#users)\n    1. [Submissions](#submissions)\n    1. [Journals](#journals)\n1. [Submission Files](#submission-files)\n1. [Upgrading Database](#upgrading-database)\n1. [Contributing](#contributing)\n1. [Issues](#issues)\n1. [Appendix](#appendix)\n\n## Installation and Update\n\nTo install the program it is sufficient to use Python pip and get the package `falocalrepo`.\n\n```shell\npython3 -m pip install falocalrepo\n```\n\nPython 3.9 or above is needed to run this program, all other dependencies are handled by pip during installation. For\ninformation on how to install Python on your computer, refer to the official\nwebsite [Python.org](https://www.python.org/).\n\nTo upgrade the `falocalrepo` and its dependencies, use pip to upgrade all three components.\n\n```shell\npython3 -m pip install --upgrade falocalrepo faapi falocalrepo-database falocalrepo-server\n```\n\nTo check for updates use the `--updates` option when launching the program. A message will be if there is an update\navailable for any component.\n\nThe program needs cookies from a logged-in FurAffinity session to download protected pages. Without the cookies the\nprogram can still download publicly available pages, but others will return empty. See [#Cookies](#cookies) for more\ndetails on which cookies to use.\n\n**Warning**: FurAffinity theme template must be set to "modern". Can be changed\nat [furaffinity.net/controls/settings/](https://www.furaffinity.net/controls/settings/).\n\n## Cookies\n\nThe scraping library used by this program needs two specific cookies from a logged-in FurAffinity session. These are\ncookie `a` and cookie `b`.\n\nAs of 2020-08-09 these take the form of hexadecimal strings like `356f5962-5a60-0922-1c11-65003b703038`.\n\nThe easiest way to obtain these cookies is by using a browser extension to extract your cookies and then search for `a`\nand `b`.<br>\nAlternatively, the storage inspection tool of a desktop browser can also be used. For example on Mozilla\'s Firefox this\ncan be opened with the &#8679;F9 shortcut.\n\nTo set the cookies use the `config cookies` command. See [#Configuration](#configuration) for more details.\n\n## Usage\n\n> **How to Read Usage Instructions**\n>  * `command` a static command keyword\n>  * `<arg>` `<param>` `<value>` an argument, parameter, value, etc... that must be provided to a command\n>  * `[<arg>]` an optional argument that can be omitted\n>  * `<arg1> | <arg2>` mutually exclusive arguments, only use one\n\nTo run the program, simply call `falocalrepo` in your shell after installation.\n\nRunning without arguments will prompt a help message with all the available options and commands.\n\nThe usage pattern for the program is as follows:\n\n```\nfalocalrepo [-h | -v | -d | -s | -u] [<command> [<operation>] [<arg1> ... <argN>]]\n```\n\nAvailable options are:\n\n* `-h, --help` show help message\n* `-v, --version` show program version\n* `-d, --database` show database version\n* `-s, --server` show server version\n* `-u, --updates` check for updates on PyPi\n\nAvailable commands are:\n\n* `help` display the manual of a command\n* `init` create the database and exit\n* `config` manage settings\n* `download` perform downloads\n* `database` operate on the database\n\n_Note:_ all the commands except `help` will create and initialise the database if it is not present in the folder\n\n_Note:_ only one instance of the program is allowed at any given time when performing download operations\n\n_Note:_ only one connection to a database is allowed at any given time, if the database is opened in other processes,\nthe program will close with an error\n\n_Note_: the program will not operate if the version of the database does not match the version of\nthe `falocalrepo-database` module. Only `database info` and `database upgrade` commands can be run if the database is\nnot up to date.\n\nWhen the database is first initialised, it defaults the submissions files folder to `FA.files`. This value can be\nchanged using the [`config` command](#configuration).\n\nCookies need to be set manually with the config command before the program will be able to access protected pages.\n\n### Environmental Variables\n\n`falocalrepo` supports the following environmental variables:\n\n* `FALOCALREPO_DATABASE` sets a path for the database rather than using the current folder. If the path basename ends\n  with `.db` -- e.g. `~/Documents/FA/MyFA.db` -- , then a database file will be created/opened with that name.\n  Otherwise, the path will be considered a folder, and a database named "FA.db" will be created therein.\n* `FALOCALREPO_DEBUG` always print traceback of caught exceptions, regardless of whether they are known or not.\n\n### Error Codes\n\nIf the program encounters a fatal error, the error is printed to `STDERR` and the program exits with a specific error\ncode:\n\n* 1 `MalformedCommand`, `UnknownCommand` command error.\n* 2 `MultipleInstances` another instance of the program was detected.\n* 3 `UnknownFolder` an unknown download folder was given to the [`download` command](#download).\n* 4 `ConnectionError` a connection error was encountered during download.\n* 5 `DatabaseError`, `IntegrityError` an error with the database file occurred.\n* 6 `TypeError`, `AssertionError` a type error was encountered.\n* 7 an unknown exception was encountered. The full traceback is saved to a `FA.log` file located in the current working\n  directory.\n\nThe exception traceback is printed only for unknown exception (error 7). Using the `FALOCALREPO_DEBUG`\n[environmental variable](#environmental-variables) forces printing of traceback for all exceptions.\n\n### Help\n\n`help [<command> [<operations>]]`\n\nThe `help` command gives information on the usage of the program and its commands and operations.\n\n> ```\n> falocalrepo help\n> ```\n> ```\n> falocalrepo help download\n> ```\n> ```\n> falocalrepo help database search-users\n> ```\n\n### Init\n\nThe `init` command initialises the database or, if one is already present, updates to a new version - if available - and\nthen exits.\n\nIt can be used to create the database and then manually edit it, or to update it to a new version without calling other\ncommands.\n\n### Configuration\n\n`config [<setting> [<value1>] ... [<valueN>]]`\n\nThe `config` command allows to change the settings used by the program.\n\nRunning the command alone will list the current values of the settings stored in the database.\nRunning `config <setting>` without value arguments will show the current value of that specific setting.\n\nAvailable settings are:\n\n* `list` list stored settings.\n* `cookies [<cookie1 name>=<cookie1 value>] ... [<cookieN name>=<cookieN value>]` the cookies stored in the database.\n\n> ```\n> falocalrepo config cookies a=38565475-3421-3f21-7f63-3d341339737 b=356f5962-5a60-0922-1c11-65003b703038\n> ```\n\n* `files-folder [<new folder>]` the folder used to store submission files. This can be any path relative to the folder\n  of the database. If a new value is given, the program will move any files to the new location.\n\n> ```\n> falocalrepo config files-folder SubmissionFiles\n> ```\n\n### Download\n\n`download <operation> [<option>=<value>] [<arg1>] ... [<argN>]`\n\nThe `download` command performs all download and repository update operations. Submission thumbnails are downloaded\nalongside the main data and are stored as `thumbnail.jpg` in the submission folder (\nsee [Submission Files](#submission-files)).\n\nAvailable operations are:\n\n* `users <user1>[,...,<userN>] <folder1>[,...,<folderN>]` download specific user folders. Requires two arguments with\n  comma-separated users and folders. Prepending `list-` to a folder allows to list all remote items in a user folder\n  without downloading them. Supported folders are:\n    * `gallery`\n    * `scraps`\n    * `favorites`\n    * `journals`\n\n> ```\n> falocalrepo download users tom,jerry gallery,scraps,journals\n> ```\n> ```\n> falocalrepo download users tom,jerry list-favorites\n> ```\n\n* `update [stop=<n>] [deactivated=<deactivated>] [<user1>,...,<userN>] [<folder1>,...,<folderN>]` update the repository\n  by checking the previously downloaded folders (gallery, scraps, favorites or journals) of each user and stopping when\n  it finds a submission that is already present in the repository. Can pass a list of users and/or folders that will be\n  updated if in the database. To skip users, use `@` as argument. The `stop=<n>` option allows to stop the update after\n  finding `n` submissions in a user\'s database entry, defaults to 1. If a user is deactivated, the folders in the\n  database will be prepended with a \'!\'. Deactivated users will be skipped when update is called, unless\n  the `<deactivated>` option is set to `true`.\n\n> ```\n> falocalrepo download update stop=5\n> ```\n> ```\n> falocalrepo download update deactivated=true @ gallery,scraps\n> ```\n> ```\n> falocalrepo download update tom,jerry\n> ```\n\n* `submissions <id1> ... [<idN>]` download specific submissions. Requires submission IDs provided as separate arguments,\n  if a submission is already in the database it is ignored.\n\n> ```\n> falocalrepo download submissions 12345678 13572468 87651234\n> ```\n\n* `journals <id1> ... [<idN>]` download specific journals. Requires journal IDs provided as separate arguments, if a\n  journal is already in the database it is ignored.\n\n> ```\n> falocalrepo download journals 123456 135724 876512\n> ```\n\n### Database\n\n`database [<operation> [<param1>=<value1> ... <paramN>=<valueN>]]`\n\nThe `database` command allows operating on the database. Used without an operation command shows the database\ninformation, statistics (number of users and submissions and time of last update), and version.\n\nAll search operations are conducted case-insensitively using the SQLite [`like`](https://sqlite.org/lang_expr.html#like)\nexpression which allows for a limited pattern matching. For example this expression can be used to search two words\ntogether separated by an unknown amount of characters `%cat%mouse%`. Fields missing wildcards will only match an exact\nresult, i.e. `cat` will only match a field equal to `cat` whereas `%cat%` wil match a field that contains `cat`.\nBars (`|`) can be used to isolate individual items in list fields.\n\nAll search operations support the extra `order`, `limit`, and `offset` parameters with values in\nSQLite [`ORDER BY` clause](https://sqlite.org/lang_select.html#the_order_by_clause)\n, [`LIMIT` clause](https://sqlite.org/lang_select.html#the_limit_clause) format,\nand [`OFFSET` clause](https://sqlite.org/lang_select.html#the_limit_clause). The `order` parameter supports all fields\nof the specific search command.\n\nAvailable operations are:\n\n* `info` show database information, statistics and version.\n* `history` show commands history\n* `search-users [json=<json>] [columns=<columns>] [<param1>=<value1>] ... [<paramN>=<valueN>]` search the users entries\n  using metadata fields. Search parameters can be passed multiple times to act as OR values. All columns of the users\n  table are supported: [#Users](#users). The `any` parameter can be used to match against any column. Parameters can be\n  lowercase. If no parameters are supplied, a list of all users will be returned instead. If `<json>` is set to \'true\',\n  the results are printed as a list of objects in JSON format. If `<columns>` is passed, then the objects printed with\n  the JSON option will only contain those fields.\n\n> ```\n> falocalrepo database search-users json=true folders=%gallery%\n> ```\n\n* `search-submissions [json=<json>] [columns=<columns>] [<param1>=<value1>] ... [<paramN>=<valueN>]` search the\n  submissions entries using metadata fields. Search parameters can be passed multiple times to act as OR values. All\n  columns of the submissions table are supported: [#Submissions](#submissions). The `any` parameter can be used to match\n  against any column. Parameters can be lowercase. If no parameters are supplied, a list of all submissions will be\n  returned instead. If `<json>` is set to \'true\', the results are printed as a list of objects in JSON format.\n  If `<columns>` is passed, then the objects printed with the JSON option will only contain those fields.\n\n> ```\n> falocalrepo database search-submissions tags=%|cat|%|mouse|% date=2020-% category=%artwork% order="AUTHOR" order="ID"\n> ```\n> ```\n> falocalrepo database search-submissions json=true columns=id,author,title author=\'CatArtist\' tags=%|cat|% tags=%|mouse|% date=2020-% category=%artwork%\n> ```\n\n* `search-journals [json=<json>] [columns=<columns>] [<param1>=<value1>] ... [<paramN>=<valueN>]` search the journals\n  entries using metadata fields. Search parameters can be passed multiple times to act as OR values. All columns of the\n  journals table are supported: [#Journals](#journals). The `any` parameter can be used to match against any column.\n  Parameters can be lowercase. If no parameters are supplied, a list of all journals will be returned instead.\n  If `<json>` is set to \'true\', the results are printed as a list of objects in JSON format. If `<columns>` is passed,\n  then the objects printed with the JSON option will only contain those fields.\n\n> ```\n> falocalrepo database search-journals date=2020-% author=CatArtist order="ID DESC"\n> ```\n> ```\n> falocalrepo database search-journals json=true columns=id,author,title date=2020-% date=2019-% content=%commission%\n> ```\n\n* `add-user <json>` Add or replace a user entry into the database using metadata from a JSON file. If the user already\n  exists in the database, fields may be omitted from the JSON, except for the ID. Omitted fields will not be replaced in\n  the database and will remain as they are. The following fields are supported:\n    * `username`<br>\n      The following fields are optional:\n    * `folders`\n\n> ```\n> falocalrepo database add-user ./user.json\n> ```\n\n* `add-submission <json> [file=<file>] [thumb=<thumb>]` Add or replace a submission entry into the database using\n  metadata from a JSON file. If the submission already exists in the database, fields may be omitted from the JSON,\n  except for the ID. Omitted fields will not be replaced in the database and will remain as they are. The\n  optional `<file>` and `<thumb>` parameters allow adding or replacing the submission file and thumbnail respectively.\n  The following fields are supported:\n    * `id`\n    * `title`\n    * `author`\n    * `date` date in the format YYYY-MM-DD\n    * `description`\n    * `category`\n    * `species`\n    * `gender`\n    * `rating`\n    * `type` image, text, music, or flash * \'folder\' gallery or scraps\n    * `fileurl` the remote URL of the submission file<br>\n      The following fields are optional:\n    * `tags` list of tags, if omitted it defaults to existing entry or empty\n    * `favorite` list of users that faved the submission, if omitted it defaults to existing entry or empty\n    * `mentions` list of mentioned users, if omitted it defaults to existing entry or mentions are extracted from the\n      description\n    * `userupdate` 1 if the submission is downloaded as part of a user gallery/scraps else 0, if omitted it defaults to\n      entry or 0\n\n> ```\n> falocalrepo database add-submission add-submission ./submission/metadata.json \\\n>     file=./submission/submission.pdf thumb=./submission/thumbnail.jpg\n> ```\n\n* `add-journal <json>` Add or replace a journal entry into the database using metadata from a JSON file. If the journal\n  already exists in the database, fields may be omitted from the JSON, except for the ID. Omitted fields will not be\n  replaced in the database and will remain as they are. The following fields are supported:\n    * `id`\n    * `title`\n    * `author`\n    * `date` date in the format YYYY-MM-DD * \'content\' the body of the journal<br>\n      The following fields are optional:\n    * `mentions` list of mentioned users, if omitted it defaults to existing entry or mentions are extracted from the\n      content\n\n> ```\n> falocalrepo database add-journal ./journal.json"\n> ```\n\n* `remove-users <user1> ... [<userN>]` remove specific users from the database.\n\n> ```\n> falocalrepo database remove-users jerry\n> ```\n\n* `remove-submissions <id1> ... [<idN>]` remove specific submissions from the database.\n\n> ```\n> falocalrepo database remove-submissions 12345678 13572468 87651234\n> ```\n\n* `remove-journals <id1> ... [<idN>]` remove specific journals from the database.\n\n> ```\n> falocalrepo database remove-journals 123456 135724 876512\n> ```\n\n* `server [host=<host>] [port=<port>]` starts a server at `<host>:<port>` to navigate the database\n  using `falocalrepo-server`. Defaults to `0.0.0.0:8080`.\n  See [falocalrepo-server](https://pypi.org/project/falocalrepo-server) for more details on usage. Running the server\n  does not occupy the database connection (it is only occupied when the server is actively searching the database),\n  which allows running other `database` commands; `download` commands remain unavailable.\n\n> ```\n> falocalrepo database server host=127.0.0.1 port=5000\n> ```\n\n* `merge <path> [<table1>.<param1>=<value1> ... <tableN>.<paramN>=<valueN>]` Merge selected entries from a second\n  database to the main database (the one opened with the program). To select entries, use the same parameters as the\n  search commands precede by a table name. Search parameters can be passed multiple times to act as OR values. All\n  columns of the entries table are supported. Parameters can be lowercase. If no parameters are passed then all the\n  database entries are copied. If submissions entries are selected, their files are copied to the files\' folder of the\n  main database.\n\n> ```\n> falocalrepo database merge ~/Documents/FA.backup/A/FA.db users.username=a% \\\n>     submissions.author=a% journals.author=a%\n> ```\n> ```\n> falocalrepo database merge ~/Documents/FA2020/FA.db submissions.date=2020-% \\\n>     journals.date=2020-%\n> ```\n> ```\n> falocalrepo database merge ~/Documents/FA.backup/FA.db\n> ```\n\n* `copy <path> [<table1>.<param1>=<value1> ... <tableN>.<paramN>=<valueN>]` Copy selected entries to a new or existing\n  database. To select entries, use the same parameters as the search commands precede by a table name. Search parameters\n  can be passed multiple times to act as OR values. All columns of the entries table are supported. Parameters can be\n  lowercase. If no parameters are passed then all the database entries are copied. If submissions entries are selected,\n  their files are copied to the files\' folder of the target database.\n\n> ```\n> falocalrepo database copy ~/Documents/FA.backup/A/FA.db users.username=a% \\\n>     submissions.author=a% journals.author=a%\n> ```\n> ```\n> falocalrepo database copy ~/Documents/FA2020/FA.db submissions.date=2020-% \\\n>     journals.date=2020-%\n> ```\n> ```\n> falocalrepo database copy ~/Documents/FA.backup/FA.db\n> ```\n\n* `clean` clean the database using the SQLite [VACUUM](https://www.sqlite.org/lang_vacuum.html) function. Requires no\n  arguments.\n* `upgrade` upgrade the database to the latest version\n\n## Database\n\nTo store the metadata of the downloaded submissions, journals, users, cookies and statistics, the program uses a SQLite3\ndatabase. This database is built to be as light as possible while also containing all the metadata that can be extracted\nfrom a submission page.\n\nTo store all this information, the database uses four tables: `SETTINGS`, `USERS`, `SUBMISSIONS` and `JOURNALS`.\n\n> **How Lists Are Stored**<br>\n> Some fields in the database table contain lists of items. These are stored as strings, with each item surrounded by\n> bars (`|`). This allows to properly separate and search individual items regardless of their position in the list.<br>\n> `|item1||item2|`<br>\n\n### Settings\n\nThe settings table contains settings for the program and statistics of the database.\n\n* `HISTORY` list of executed commands in the format `[[<time1>, "<command1>"], ..., [<timeN>, "<commandN>"]]` (UNIX time\n  in seconds)\n* `COOKIES` cookies for the scraper, stored in JSON format\n* `FILESFOLDER` location of downloaded submission files\n* `VERSION` database version, this can differ from the program version\n\n### Users\n\nThe users table contains a list of all the users that have been download with the program, the folders that have been\ndownloaded, and the submissions found in each of those.\n\nEach entry contains the following fields:\n\n* `USERNAME` The URL username of the user (no underscores or spaces)\n* `FOLDERS` the folders downloaded for that specific user, sorted and bar-separated\n\n### Submissions\n\nThe submissions table contains the metadata of the submissions downloaded by the program and information on their files\n\n* `ID` the id of the submission\n* `AUTHOR` the username of the author (uploader) in full format\n* `TITLE`\n* `DATE` upload date in ISO format YYYY-MM-DD**T**HH:MM\n* `DESCRIPTION` description in html format\n* `TAGS` keywords sorted alphanumerically and bar-separated\n* `CATEGORY`\n* `SPECIES`\n* `GENDER`\n* `RATING`\n* `TYPE` image, text, music, or flash\n* `FILEURL` the remote URL of the submission file\n* `FILEEXT` the extensions of the downloaded file. Can be empty if the file contained errors and could not be recognised\n  upon download\n* `FILESAVED` file and thumbnail download status: 00, 01, 10, 11. 1*x* if the file was downloaded 0*x* if not, *x*1 if\n  thumbnail was downloaded, *x*0 if not\n* `FAVORITE` a bar-separated list of users that have "faved" the submission\n* `MENTIONS` a bar-separated list of users that are mentioned in the submission description as links\n* `FOLDER` the folder of the submission (`gallery` or `scraps`)\n* `USERUPDATE` whether the submission was added as a user update or favorite/single entry\n\n### Journals\n\nThe journals table contains the metadata of the journals downloaded by the program.\n\n* `ID` the id of the journal\n* `AUTHOR` the username of the author (uploader) in full format\n* `TITLE`\n* `DATE` upload date in ISO format YYYY-MM-DD**T**HH:MM\n* `CONTENT` content in html format\n* `MENTIONS` a bar-separated list of users that are mentioned in the journal content as links\n* `USERUPDATE` whether the journal was added as a user update or single entry\n\n## Submission Files\n\nSubmission files are saved in a tiered tree structure based on their submission ID. IDs are zero-padded to 10 digits and\nthen broken up in 5 segments of 2 digits; each of these segments represents a folder tha will be created in the tree.\n\nFor example, a submission `1457893` will be padded to `0001457893` and divided into `00`, `01`, `45`, `78`, `93`. The\nsubmission file will then be saved as `00/01/45/78/93/submission.file` with the correct extension extracted from the\nfile itself - FurAffinity links do not always contain the right extension.\n\n## Upgrading Database\n\nWhen the program starts, it checks the version of the database against the one used by the program and if the latter is\nmore advanced it upgrades the database.\n\n_Note:_ Versions before 2.7.0 are not supported by falocalrepo version 3.0.0 and above. To update from those to the new\nversion use version 2.11.2 to update the database to version 2.7.0\n\nFor details on upgrades and changes between database versions,\nsee [falocalrepo-database](https://pypi.org/project/falocalrepo-database/).\n\n## Contributing\n\nAll contributions and suggestions are welcome!\n\nThe only requirement is that any merge request must be sent to the GitLab project as the one on GitHub is only a\nmirror: [GitLab/FALocalRepo](https://gitlab.com/MatteoCampinoti94/FALocalRepo)\n\nIf you have suggestions for fixes or improvements, you can open an issue with your idea, see [#Issues](#issues) for\ndetails.\n\n## Issues\n\nIf any problem is encountered during usage of the program, an issue can be opened on the project\'s pages\non [GitLab](https://gitlab.com/MatteoCampinoti94/FALocalRepo/issues) (preferred)\nor [GitHub](https://github.com/MatteoCampinoti94/FALocalRepo/issues) (mirror repository).\n\nIssues can also be used to suggest improvements and features.\n\nWhen opening an issue for a problem, please copy the error message and describe the operation in progress when the error\noccurred.\n\n## Appendix\n\n### Earlier Releases\n\nRelease 3.0.0 was deleted from PyPi because of an error in the package information. However, it can still be found in\nthe code repository under tag [v3.0.0](https://gitlab.com/MatteoCampinoti94/FALocalRepo/tags/v3.0.0).\n\nRelease binaries for versions 2.11.x can be found on GitLab\nat [FALocalRepo/tags 2.11](https://gitlab.com/MatteoCampinoti94/FALocalRepo/tags?search=v2.11).\n\nRelease binaries before and including 2.10.2 can be found\nin [GitHub Releases](https://github.com/MatteoCampinoti94/FALocalRepo/releases).\n',
    'author': 'Matteo Campinoti',
    'author_email': 'matteo.campinoti94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/MatteoCampinoti94/FALocalRepo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
