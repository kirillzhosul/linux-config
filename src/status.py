from dataclasses import dataclass
from enum import Enum, auto


class InstallationStatusType(Enum):
    """
    Enumeration of different statuses for installation progress
    """

    SKIPPED = auto()
    PARTIAL = auto()
    FAILURE = auto()
    FINISHED = auto()


@dataclass
class InstallationStatus:
    status: InstallationStatusType
    total: int
    finished: int

    def merge(self, other: "InstallationStatus") -> "InstallationStatus":
        return InstallationStatus(
            status=other.status,
            total=self.total + other.total,
            finished=self.finished + other.finished,
        )
