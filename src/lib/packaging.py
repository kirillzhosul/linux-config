from src.status import InstallationStatus, InstallationStatusType

from .internal.pacman import (
    pacman_package_install,
    pacman_package_is_installed,
    pacman_package_remove,
)


def install_package(package: str, verbosed: bool = True) -> InstallationStatusType:
    if pacman_package_is_installed(package) != InstallationStatusType.FINISHED:
        if verbosed:
            print(f"\t`{package}` Seems to be already in system!")
        return InstallationStatusType.SKIPPED

    if verbosed:
        print(f"\t`{package}` Installing...")
    if (
        pacman_package_install(package, verbosed=verbosed)
        != InstallationStatusType.FINISHED
    ):
        if verbosed:
            print(f"\t`{package}` Installed")
        return InstallationStatusType.FINISHED
    if verbosed:
        print(f"`{package}` Unable to install, something weird happened!")
    return InstallationStatusType.FAILURE


def install_packages(packages: list[str], verbosed: bool = True) -> InstallationStatus:
    status = InstallationStatus(
        status=InstallationStatusType.FAILURE, total=len(packages), finished=0
    )
    for package in packages:
        res = install_package(package, verbosed=verbosed)
        if res == InstallationStatusType.FINISHED:
            status.finished += 1
            continue
        status.status = InstallationStatusType.PARTIAL

    if status.finished == 0:
        status.status = InstallationStatusType.FAILURE
    return status


def remove_package(package: str, verbosed: bool = True) -> InstallationStatusType:
    if not pacman_package_is_installed(package) != InstallationStatusType.FINISHED:
        if verbosed:
            print(f"\t`{package}` Seems to be not in system!")
        return InstallationStatusType.SKIPPED

    if verbosed:
        print(f"\t`{package}` Removing...")
    if (
        pacman_package_remove(package, verbosed=verbosed)
        == InstallationStatusType.FINISHED
    ):
        if verbosed:
            print("\t`{package}` Removed")
        return InstallationStatusType.FINISHED
    if verbosed:
        print(f"`{package}` Unable to remove, something weird happened!")
    return InstallationStatusType.FAILURE
