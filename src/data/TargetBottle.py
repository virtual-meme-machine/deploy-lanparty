import abc
import os
import subprocess

from data.InstallTarget import InstallTarget
from utils.flatpak_utils import FLATPAK_EXEC, install_flatpaks, is_flatpak_installed

BOTTLES_IDENTIFIER: str = "com.usebottles.bottles"
BOTTLES_CLI_EXEC: list[str] = [FLATPAK_EXEC, "run", "--command=bottles-cli", BOTTLES_IDENTIFIER]


class TargetBottle(InstallTarget, abc.ABC):
    """
    Installation target that is installed via Bottles
    """

    def __init__(self,
                 name: str,
                 description: str,
                 identifier: str,
                 requires_additional_data: bool,
                 additional_data_file: str or None):
        """
        Installation target that is installed via Bottles
        :param name: Target's name, example: "Counter-Strike 1.6"
        :param description: Target's description, example: "Classic Counter-Strike at its best"
        :param requires_additional_data: Denotes if this target requires additional data to function
        :param identifier: Target's Bottle name, example: "counterstrike-16"
        :param additional_data_file: Name of a zip file containing data required for the target, example: "cs16.zip"
        """
        self.name = name
        self.description = description
        self.identifier = identifier
        self.requires_additional_data = requires_additional_data
        self.additional_data_file = additional_data_file
        self.target_root = os.path.join(os.path.expanduser(f"~/.var/app/{BOTTLES_IDENTIFIER}/data/bottles/bottles"),
                                        self.identifier,
                                        "drive_c")

    @staticmethod
    def setup_bottles():
        """
        Requests the user preform the initial Bottles setup and launched Bottles
        :return: None
        """
        runners = os.path.expanduser(path=f"~/.var/app/{BOTTLES_IDENTIFIER}/data/bottles/runners")
        if not os.path.isdir(s=runners):
            print(f"Bottles has not been setup yet, please click through the initial setup and then exit Bottles")
            subprocess.run(args=["/usr/bin/killall", "bottles"])
            subprocess.run(args=[FLATPAK_EXEC, "run", BOTTLES_IDENTIFIER],
                           check=True)

    def install(self):
        """
        Creates a new Bottle for the target
        :return: None
        """
        if not is_flatpak_installed(flatpak_id=BOTTLES_IDENTIFIER):
            install_flatpaks(flatpak_list=[BOTTLES_IDENTIFIER])

        self.setup_bottles()

        if os.path.isdir(s=self.target_root):
            print(f"Bottle '{self.identifier}' already exists")
            return

        subprocess.run(args=BOTTLES_CLI_EXEC + ["new",
                                                "--bottle-name", self.identifier,
                                                "--environment", "gaming"],
                       check=True)

    def add_program(self, name: str, path: str, launch_options: str):
        """
        Registers a program with the Bottle
        :param name: Name of the program, example: "Counter-Strike 1.6"
        :param path: Path to the program exec, example: f"{target_root}/Half-Life/hl.exe"
        :param launch_options: Launch options the program should launch with, example: "-game cstrike"
        :return: None
        """
        bottle_programs = subprocess.run(args=BOTTLES_CLI_EXEC + ["programs", "--bottle", self.identifier],
                                         capture_output=True,
                                         check=True).stdout.decode().strip()

        if name in bottle_programs:
            print(f"Program already added to Bottle")
            return

        subprocess.run(args=BOTTLES_CLI_EXEC + ["add",
                                                "--bottle", self.identifier,
                                                "--name", name,
                                                "--path", path,
                                                "--launch-options", launch_options],
                       check=True)
        print("")  # Print a blank line here because Bottles doesn't print a line end when it's done

    def create_desktop_file(self):
        """
        Creates a .desktop file for a program in a Bottle
        :return: None
        """
        desktop_file = os.path.expanduser(path=f"~/.local/share/applications/{self.identifier}.desktop")
        desktop_lines = [
            f"[Desktop Entry]",
            f"Name={self.name}",
            f"Exec=flatpak run --command=bottles-cli com.usebottles.bottles run -p '{self.name}' -b '{self.identifier}' -- %u",
            f"Type=Application",
            f"Terminal=false",
            f"Categories=Application;",
            # f"Icon={os.path.expanduser(f"~/.var/app/com.usebottles.bottles/data/bottles/bottles/{self.identifier}/icons/{self.name}.png")}",
            f"Comment=Launch {self.name} using Bottles.",
            f"StartupWMClass={self.name}",
            f"Actions=Configure;",
            f"[Desktop Action Configure]",
            f"Name=Configure in Bottles",
            f"Exec=flatpak run com.usebottles.bottles -b '{self.identifier}'",
        ]

        if os.path.isfile(path=desktop_file):
            print(f".desktop file already exists")
            return

        print("Creating .desktop file")
        with open(file=desktop_file, mode="w") as desktop_file:
            for line in desktop_lines:
                desktop_file.write(line)
                desktop_file.write("\n")
