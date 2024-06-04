from src.targets.base_target import BaseTarget


class FontsInstaller(BaseTarget):
    REQUIRED_PACKAGES = ["ttf-jetbrains-mono-nerd", "ttf-firacode-nerd"]
