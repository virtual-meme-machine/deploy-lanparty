from data.TargetFlatpak import TargetFlatpak


class SRB2K(TargetFlatpak):
    """
    Installs Sonic Robo Blast 2 Kart
    """

    def __init__(self):
        """
        Installs Sonic Robo Blast 2 Kart
        """
        super().__init__(name="Sonic Robo Blast 2 Kart",
                         description="Genesis era Sonic themed kart racer with online multiplayer",
                         identifier="org.srb2.SRB2Kart",
                         requires_additional_data=False,
                         additional_data_file=None)

    def configure(self):
        """
        Does nothing, no configuration required
        :return: None
        """
        pass
