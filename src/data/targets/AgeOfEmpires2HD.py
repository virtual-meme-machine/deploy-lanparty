import os.path
import shutil

from data.TargetBottle import TargetBottle
from utils.game_utils import install_steam_emulator


class AgeOfEmpires2HD(TargetBottle):
    """
    Installs Age of Empires II HD (2013)
    """

    def __init__(self):
        """
        Installs Age of Empires II HD (2013)
        """
        super().__init__(name="Age of Empires II HD (2013)",
                         description="Updated HD release of Age of Empires II",
                         identifier="aoe2hd",
                         requires_additional_data=True,
                         additional_data_file="aoe2hd.zip")

    def configure(self):
        """
        Configures Age of Empires II HD (2013) by doing the following:
        - Copies DirectX DLL files to the root of game data folder
        - Installs Steam emulator allowing for LAN play without Steam installed
        - Creates program entry in Bottles
        - Creates a .desktop file
        :return: None
        """
        if os.path.isfile(os.path.join(self.target_root, "Age2HD/d3dx9_43.dll")):
            print("DirectX DLL files already exist")
        else:
            print("Copying DirectX DLL files to game data root")
            d3d9_dlls_folder = os.path.join(self.target_root, "Age2HD/D3D9_DLLBACKUP")
            for d3d9_dll in os.listdir(path=d3d9_dlls_folder):
                shutil.copy2(src=os.path.join(d3d9_dlls_folder, d3d9_dll),
                             dst=os.path.join(self.target_root, "Age2HD", d3d9_dll))

        install_steam_emulator(target_directory=f"{self.target_root}/Age2HD",
                               steam_app_id=221380)

        self.add_program(name=self.name,
                         path=os.path.join(self.target_root, "Age2HD/AoK HD.exe"))

        self.create_desktop_file()
