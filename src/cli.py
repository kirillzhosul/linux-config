"""
Command line interface provider
"""

from sys import argv

from .targets import InstallerManager, get_target_installers


def cli_show_header() -> None:
    # fmt: off
    print(" ___      ___   __    _  __   __  __   __    _______  _______  __    _  _______  ___   _______ ")
    print("|   |    |   | |  |  | ||  | |  ||  |_|  |  |       ||       ||  |  | ||       ||   | |       |")
    print("|   |    |   | |   |_| ||  | |  ||       |  |       ||   _   ||   |_| ||    ___||   | |    ___|")
    print("|   |    |   | |       ||  |_|  ||       |  |       ||  | |  ||       ||   |___ |   | |   | __ ")
    print("|   |___ |   | |  _    ||       | |     |   |      _||  |_|  ||  _    ||    ___||   | |   ||  |")
    print("|       ||   | | | |   ||       ||   _   |  |     |_ |       || | |   ||   |    |   | |   |_| |")
    print("|_______||___| |_|  |__||_______||__| |__|  |_______||_______||_|  |__||___|    |___| |_______|")
    print()
    print("\tLinux Config - configuration tool for my system")
    print("\tNo warranties given, use at your own risk!")
    print("\t(c) Kirill Zhosul")
    print()
    print()
    # fmt: on


def cli_usage() -> None:
    print("\tNo command supplied! Please use like `linux-config <command> [args]`!")
    print("\tNote: use `help` command/subcommand for described usage")


def cli_global_help() -> None:
    print("\tCommands:")
    print("\t\tcheck: Validate current configs in system")
    print("\t\tinject|push: Inject configs and applications into system")
    print("\t\thelp: this message")


def cli_unknown_command() -> None:
    print("\tUnknown command! Please use `help` for all commands!")


def cli_entry_point() -> None:
    _, *args = argv

    cli_show_header()

    if not args:
        cli_usage()
        exit(1)

    command, *args = args

    subcommand = ""
    if args:
        subcommand, *args = args

    installers = get_target_installers()
    match command:
        case "check":
            if subcommand == "help":
                exit(1)
            exit(1)
        case "inject" | "push":
            if subcommand == "help":
                exit(1)
            print("\tInjecting configs...")

            status = InstallerManager(installers).install()

            print(f"\t{status}")
            print("\tFinished injecting!")
        case "help":
            cli_global_help()
        case _:
            cli_unknown_command()

    # install_all()
