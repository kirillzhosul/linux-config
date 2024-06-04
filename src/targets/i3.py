from src.targets.base_target import BaseTarget


class I3Installer(BaseTarget):
    REQUIRED_PACKAGES = ["i3-wm"]
    COPIED_PATHS = [
        ("./configs/i3/config", "/etc/i3/config"),
        ("./configs/i3/config", "~/.config/i3/config"),
    ]
