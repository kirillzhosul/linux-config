import os


def system_mark_as_executable_file(path: str) -> None:
    """
    Marks given path as executable file
    """
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2  # copy R bits to X
