import configparser
import os

from data.TargetFlatpak import TargetFlatpak


class OpenRCT2(TargetFlatpak):
    """
    Installs OpenRCT2
    """

    def __init__(self):
        """
        Installs OpenRCT2
        """
        super().__init__(name="OpenRCT2",
                         description="Open-source re-implementation of Roller Coaster Tycoon 2",
                         identifier="io.openrct2.OpenRCT2",
                         requires_additional_data=True,
                         additional_data_file="openrct2.zip")

    def configure(self):
        """
        Configures OpenRCT2 by doing the following:
        - Moves game data to data search paths
        - Update config file to point to game data
        :return: None
        """
        self.move_game_data(source_paths=[os.path.join(self.target_root, "rct2")],
                            target_path=os.path.join(self.target_root, "config/OpenRCT2"),
                            check_path=os.path.join(self.target_root, "config/OpenRCT2/rct2"))
        self.update_config_file()

    def update_config_file(self):
        """
        Updates the OpenRCT2 config file to point to the game data location
        :return: None
        """
        target_path = os.path.join(self.target_root, "config/OpenRCT2")
        config_file_path = os.path.join(target_path, "config.ini")
        game_path = f"\"{os.path.join(target_path, "rct2/app")}\""
        config = configparser.ConfigParser()

        if os.path.isfile(config_file_path):
            config.read(config_file_path)

        if config.get(section="general", option="game_path", fallback=None) == game_path:
            print("Config file already points to game data")
            return

        print(f"Setting game data location in config file")
        if not config.has_section(section="general"):
            config.add_section("general")
        config.set(section="general", option="game_path", value=game_path)
        with open(file=config_file_path, mode="w") as config_file:
            config.write(fp=config_file)
