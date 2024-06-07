import os

from data.TargetFlatpak import TargetFlatpak


class ioquake3(TargetFlatpak):
    """
    Installs ioquake3
    """

    def __init__(self):
        """
        Installs ioquake3
        """
        super().__init__(name="ioquake3",
                         description="Open-source port of Quake 3: Arena",
                         identifier="org.ioquake3.ioquake3",
                         requires_additional_data=True,
                         additional_data_file="quake3.zip")

    def configure(self):
        """
        Configures ioquake3 by doing the following:
        - Moves Quake 3 game data to data search paths
        :return: None
        """
        self.move_game_data(source_paths=[os.path.join(self.target_root, "baseq3"),
                                          os.path.join(self.target_root, "missionpack")],
                            target_path=os.path.join(self.target_root, "data"),
                            check_path=os.path.join(self.target_root, "data/baseq3"))
