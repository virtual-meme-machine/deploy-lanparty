import os.path

from data.TargetBottle import TargetBottle
from utils.game_utils import install_steam_emulator


class CounterStrike16(TargetBottle):
    """
    Installs Counter-Strike 1.6
    """

    def __init__(self):
        """
        Installs Counter-Strike 1.6
        """
        super().__init__(name="Counter-Strike 1.6",
                         description="Classic Counter-Strike at its best",
                         identifier="counterstrike-16",
                         requires_additional_data=True,
                         additional_data_file="counterstrike-16.zip")

    def configure(self):
        """
        Configures Counter-Strike 1.6 by doing the following:
        - Installs Steam emulator allowing for LAN play without Steam installed
        - Creates program entry in Bottles
        - Creates a .desktop file
        :return: None
        """
        install_steam_emulator(target_directory=f"{self.target_root}/Half-Life",
                               steam_app_id=10)

        self.add_program(name=self.name,
                         path=os.path.join(self.target_root, "Half-Life/hl.exe"),
                         launch_options="-game cstrike")

        self.create_desktop_file()
