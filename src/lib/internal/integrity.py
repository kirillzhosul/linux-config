import hashlib


def get_file_integrity_hash(path: str) -> str | None:
    """
    Returns hash of the file for checking integrity
    """
    try:
        return hashlib.md5(open(path, "rb").read()).hexdigest()
    except FileNotFoundError:
        return
