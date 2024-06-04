import shutil
from abc import ABC

from src.lib.internal.integrity import get_file_integrity_hash
from src.lib.packaging import install_packages
from src.status import InstallationStatus, InstallationStatusType


class BaseTarget(ABC):
    """
    Target installer, contains directives how to install, configure and rollback changes in system
    Like, code editor intsaller

    """

    # Name of the installation, required
    NAME: str | None = None

    # List of package names for package manager, will be auto-installed and rolled back
    REQUIRED_PACKAGES: list[str] | None = None

    # Lis of package names for package manager that is orphans for that installation
    # mostly used for stuff that is not required but may be installed in system
    ORPHANS_PACKAGES: list[str] | None = None

    # Paths where and from copy configurations (or anything, but mostly - configuration)
    COPIED_PATHS: list[tuple[str, str]] | None = None

    def install(self) -> InstallationStatus:
        """
        Installs required packages and configuration
        """

        status = self._install_packages()
        self._copy_configuration()

        return status
        # if ret == False:  # noqa: E712
        #    ...
        #
        # ret &= self._copy_configuration()
        #
        # return ret

    def _install_packages(self) -> InstallationStatus:
        """
        Install package manager packages into system
        """
        if not self.REQUIRED_PACKAGES:
            print(
                f"\t[{self.NAME}] packages not listed, skipping installing packages..."
            )
            return InstallationStatus(
                status=InstallationStatusType.SKIPPED, total=0, finished=0
            )

        return install_packages(self.REQUIRED_PACKAGES)

    def _copy_configuration(self) -> bool:
        if not self.COPIED_PATHS:
            return True
        for path in self.COPIED_PATHS:
            a, b = path

            if get_file_integrity_hash(a) == get_file_integrity_hash(b):
                print("File hashes are same, skipping copying...")
                continue

            print(f"Copying {a} to {b}")
            shutil.copyfile(a, b)
            print("Copied!")
        return True

    # def _post_remove_orphans(self) -> bool:
    #    if self.ORPHANS_PACKAGES is not None:
    #        for package in self.ORPHANS_PACKAGES:
    #            if not remove_verbosed(package):
    #                return False
    #    return True
    #
    # def _uninstall_packages(self) -> bool:
    #    if self.REQUIRED_PACKAGES is not None:
    #        for package in self.REQUIRED_PACKAGES:
    #            if not remove_verbosed(package):
    #                return False
    #        return True
    #    raise NotImplementedError(
    #        "`REQUIRED_PACKAGES` is not defined, pass empty list or list of requirements"
    #    )
