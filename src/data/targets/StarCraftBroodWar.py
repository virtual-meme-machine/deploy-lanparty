import os

from data.TargetBottle import TargetBottle


class StarCraftBroodWar(TargetBottle):
    """
    Installs StarCraft: Brood War
    """

    def __init__(self):
        """
        Installs StarCraft: Brood War
        """
        super().__init__(name="StarCraft: Brood War",
                         description="Last version of StarCraft: Brood War before the HD remaster",
                         identifier="starcraft-bw",
                         requires_additional_data=True,
                         additional_data_file="starcraft-bw.zip")

    def configure(self):
        """
        Configures StarCraft: Brood War by doing the following:
        - Creates program entry in Bottles
        - Creates a .desktop file
        :return: None
        """
        self.add_program(name=self.name,
                         path=os.path.join(self.target_root, "StarCraft/StarCraft.exe"))

        self.create_desktop_file()
