import sys


def print_info() -> None:
    print(
        "Type annotations for boto3.Snowball 1.17.69\n"
        "Version:         1.17.69.0\n"
        "Builder version: 4.10.0\n"
        "Docs:            https://pypi.org/project/mypy-boto3-snowball/\n"
        "Boto3 docs:      https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/snowball.html#Snowball\n"
        "Other services:  https://pypi.org/project/boto3-stubs/\n"
        "Changelog:       https://github.com/vemel/mypy_boto3_builder/releases"
    )


def print_version() -> None:
    print("1.17.69.0")


def main() -> None:
    if "--version" in sys.argv:
        return print_version()
    print_info()


if __name__ == "__main__":
    main()
