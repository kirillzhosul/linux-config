from src.status import InstallationStatus, InstallationStatusType
from src.targets.base_target import BaseTarget
from src.targets.fonts import FontsInstaller
from src.targets.i3 import I3Installer
from src.targets.polybar import PolybarInstaller


def get_target_installers() -> list[BaseTarget]:
    return [FontsInstaller(), PolybarInstaller(), I3Installer()]


class InstallerManager:
    def __init__(self, targets: list[BaseTarget] | None = None) -> None:
        self.targets = targets if targets else get_target_installers()

    def install(self) -> InstallationStatus:
        status = InstallationStatus(
            status=InstallationStatusType.SKIPPED, total=0, finished=0
        )
        for target in self.targets:
            res = target.install()
            status.total += res.total
            status.finished += res.finished
            if res.status == InstallationStatusType.FINISHED:
                status.status = InstallationStatusType.PARTIAL

        if status.total == status.finished:
            status.status = InstallationStatusType.FINISHED
        return status
