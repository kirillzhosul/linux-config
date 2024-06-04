from src.targets.base_target import BaseTarget


class PolybarInstaller(BaseTarget):
    REQUIRED_PACKAGES = ["polybar"]
    ORPHANS_PACKAGES = ["xfce4-whiskermenu-plugin", "xfce4-panel"]
    COPIED_PATHS = [
        ("./configs/polybar/launch.sh", "/etc/polybar/launch.sh"),
        ("./configs/polybar/desktop.desktop", "/etc/xdg/autostart/polybar.desktop"),
        ("./configs/polybar/config.ini", "/etc/polybar/config.ini"),
    ]


# os.makedirs("/etc/polybar", exist_ok=True)
