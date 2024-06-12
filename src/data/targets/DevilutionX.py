import configparser
import os
import shutil

from data.TargetFlatpak import TargetFlatpak


class DevilutionX(TargetFlatpak):
    """
    Installs DevilutionX
    """

    def __init__(self):
        """
        Installs DevilutionX
        """
        super().__init__(name="DevilutionX",
                         description="Open-source re-implementation of Diablo and Hellfire",
                         identifier="org.diasurgical.DevilutionX",
                         requires_additional_data=False,
                         additional_data_file="devilutionx.zip")

    def configure(self):
        """
        Configures DevilutionX by doing the following:
        - Moves game data to data search paths
        - Update config file to point to game data
        :return: None
        """
        hellfire_path = os.path.join(self.target_root, "hellfire")
        source_paths = [os.path.join(self.target_root, "DIABDAT.MPQ")]
        if os.path.exists(path=hellfire_path):
            source_paths.append(os.path.join(hellfire_path, "hellfire.mpq"))
            source_paths.append(os.path.join(hellfire_path, "hfmonk.mpq"))
            source_paths.append(os.path.join(hellfire_path, "hfmusic.mpq"))
            source_paths.append(os.path.join(hellfire_path, "hfvoice.mpq"))

        self.move_game_data(source_paths=source_paths,
                            target_path=os.path.join(self.target_root, "data/diasurgical/devilution"),
                            check_path=os.path.join(self.target_root, "data/diasurgical/devilution/DIABDAT.MPQ"))
        self.update_config_file()

        if os.path.exists(path=hellfire_path) and os.path.isdir(s=hellfire_path):
            shutil.rmtree(path=hellfire_path)

    def update_config_file(self):
        """
        Updates the DevilutionX config to enable QOL features
        :return: None
        """
        config_file_path = os.path.join(self.target_root, "data/diasurgical/devilution/diablo.ini")
        config_values = [
            "MultiplayerFullQuests",
            "Run in Town",
            "Quick Cast",
            "Experience Bar",
            "Show Item Graphics in Stores",
            "Show health values",
            "Show mana values",
            "Enemy Health Bar",
            "Show Monster Type",
            "Show Item Labels",
            "Enable floating numbers",
            "Auto Refill Belt",
            "Auto Gold Pickup",
            "Adria Refills Mana"
        ]

        print("Enabling QOL features in config file")
        config = configparser.ConfigParser()
        if os.path.isfile(config_file_path):
            config.read(config_file_path)

        if not config.has_section(section="Game"):
            config.add_section("Game")

        for value in config_values:
            config.set(section="Game", option=value, value="1")

        with open(file=config_file_path, mode="w") as config_file:
            config.write(fp=config_file)
