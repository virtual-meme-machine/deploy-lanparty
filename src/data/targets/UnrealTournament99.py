import os

from data.TargetFlatpak import TargetFlatpak


class UnrealTournament99(TargetFlatpak):
    """
    Installs Unreal Tournament GOTY (1999)
    """

    def __init__(self):
        """
        Installs Unreal Tournament GOTY (1999)
        """
        super().__init__(name="Unreal Tournament GOTY (1999)",
                         description="The original Unreal Tournament in all of its 1999 glory",
                         identifier="com.epicgames.ut99",
                         requires_additional_data=True,
                         additional_data_file="unreal-tournament-99.zip")

    def configure(self):
        """
        Configures Unreal Tournament GOTY (1999) by doing the following:
        - Moves game data to data search paths
        :return: None
        """
        game_data_dir = os.path.join(self.target_root, "Unreal Tournament GOTY")
        self.move_game_data(source_paths=[os.path.join(game_data_dir, path) for path in os.listdir(game_data_dir)],
                            target_path=os.path.join(self.target_root, "data"),
                            check_path=os.path.join(self.target_root, "data/System"))
