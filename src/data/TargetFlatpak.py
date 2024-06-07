import abc
import os.path

from data.InstallTarget import InstallTarget
from utils.flatpak_utils import install_flatpaks


class TargetFlatpak(InstallTarget, abc.ABC):
    """
    Installation target that is installed via Flatpak
    """

    def __init__(self,
                 name: str,
                 description: str,
                 identifier: str,
                 requires_additional_data: bool,
                 additional_data_file: str or None):
        """
        Installation target that is installed via Flatpak
        :param name: Target's name, example: "OpenRCT2"
        :param description: Target's description, example: "Open-source re-implementation of Roller Coaster Tycoon 2"
        :param identifier: Target's Flatpak identifier, example: "io.openrct2.OpenRCT2"
        :param requires_additional_data: Denotes if this target requires additional data to function
        :param additional_data_file: Name of a zip file containing data required for the target, example: "rct2.zip"
        """
        self.name = name
        self.description = description
        self.identifier = identifier
        self.requires_additional_data = requires_additional_data
        self.additional_data_file = additional_data_file
        self.target_root = os.path.expanduser(path=f"~/.var/app/{self.identifier}")

    def install(self):
        """
        Installs the target via Flatpak
        :return: None
        """
        install_flatpaks(flatpak_list=[self.identifier])
