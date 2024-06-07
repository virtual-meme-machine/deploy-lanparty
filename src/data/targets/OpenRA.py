import os

from data.TargetFlatpak import TargetFlatpak


class OpenRA(TargetFlatpak):
    """
    Installs OpenRA
    """

    def __init__(self):
        """
        Installs OpenRA
        """
        super().__init__(name="OpenRA",
                         description="Open-source re-implementation of Command & Conquer, Red Alert, and Dune 2000",
                         identifier="net.openra.OpenRA",
                         requires_additional_data=False,
                         additional_data_file="openra.zip")

    def configure(self):
        """
        Configures OpenRA by doing the following:
        - Moves game data to data search paths
        :return: None
        """
        self.move_game_data(source_paths=[os.path.join(self.target_root, "Content")],
                            target_path=os.path.join(self.target_root, ".openra"),
                            check_path=os.path.join(self.target_root, ".openra/Content"))
