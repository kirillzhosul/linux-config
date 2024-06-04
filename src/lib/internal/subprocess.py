import os
import subprocess

from src.status import InstallationStatusType


def execute_and_return_plain(args: list[str], verbosed: bool = False) -> int:
    """
    Executes subprocess with given args and return status code
    """
    stdout, stderr = None, None
    if not verbosed:
        stdout = open(os.devnull, "w")
        stderr = subprocess.STDOUT

    return subprocess.call(
        args,
        stdout=stdout,
        stderr=stderr,
    )


def execute_and_return(
    args: list[str], verbosed: bool = False
) -> InstallationStatusType:
    """
    Executes subprocess with given commands installation status type
    """
    return wrap_execution_status(execute_and_return_plain(args, verbosed))


def wrap_execution_status(status: int) -> InstallationStatusType:
    """
    Wraps native status code into installation status code
    """
    return (
        InstallationStatusType.FINISHED
        if status == 0
        else InstallationStatusType.FAILURE
    )
