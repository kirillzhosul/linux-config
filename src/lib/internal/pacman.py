"""
Internal interface for calling pacman package manager
"""

from src.status import InstallationStatusType

from .subprocess import execute_and_return


def pacman_package_is_installed(package: str, verbosed: bool = False) -> bool:
    """
    Returns is package presented in system with pacman
    """
    return (
        execute_and_return(["pacman", "-Qi", package], verbosed=verbosed)
        == InstallationStatusType.FINISHED
    )


def pacman_package_install(
    package: str, verbosed: bool = True
) -> InstallationStatusType:
    """
    Install package with pacman
    """
    return execute_and_return(
        ["pacman", "-S", package, "--noconfirm"], verbosed=verbosed
    )


def pacman_package_remove(
    package: str, verbosed: bool = True
) -> InstallationStatusType:
    """
    Removes package from system with pacman
    """
    return execute_and_return(
        ["pacman", "-R", package, "--noconfirm"], verbosed=verbosed
    )
