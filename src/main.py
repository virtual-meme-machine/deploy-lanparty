#!/usr/bin/env python3
import os
import platform
import sys

from data.InstallTarget import InstallTarget
from data.targets.CounterStrike16 import CounterStrike16
from data.targets.OpenRA import OpenRA
from data.targets.OpenRCT2 import OpenRCT2
from data.targets.SRB2K import SRB2K
from data.targets.StarCraftBroodWar import StarCraftBroodWar
from data.targets.UnrealTournament99 import UnrealTournament99
from data.targets.ioquake3 import ioquake3
from utils.caffeine_utils import activate_caffeine, deactivate_caffeine
from utils.flatpak_utils import install_flatpaks, is_flatpak_installed
from utils.zenity_utils import set_use_cli_prompts

COMMUNICATION_APP_IDENTIFIER: str = "org.jitsi.jitsi-meet"
TARGETS: list[InstallTarget] = [
    CounterStrike16(),
    ioquake3(),
    OpenRA(),
    OpenRCT2(),
    SRB2K(),
    StarCraftBroodWar(),
    UnrealTournament99()
]


def main():
    """
    Bootstraps LAN party environment to the host by preforming the following actions:
    - Installs a communications app for voice chat
    - Installs required dependencies such as Bottles
    - Installs and configures all available targets
    :return: None
    """
    # Verify host is running Linux
    operating_system = platform.system()
    if operating_system != "Linux":
        print(f"This script does not support OS: {operating_system}")
        exit(200)

    # Activate caffeine to prevent host from going to sleep
    activate_caffeine()

    # Force usage of CLI prompts
    set_use_cli_prompts(value=True)

    # Install communication app
    if not is_flatpak_installed(flatpak_id=COMMUNICATION_APP_IDENTIFIER):
        install_flatpaks(flatpak_list=[COMMUNICATION_APP_IDENTIFIER])

    # Get data folder from args
    data_folder = os.path.expanduser(path=sys.argv[1]) if len(sys.argv) > 1 else None

    # Install targets
    index = 0
    for target in TARGETS:
        index += 1
        header = f"[{index}/{len(TARGETS)} - {target.name}]"

        try:
            print(f"\033[94m\033[1m"
                  f"{header} Installing target"
                  f"\033[0m")

            if target.requires_additional_data and data_folder is None:
                print(f"Cannot install target, additional data file is required")
                continue

            target.install()
            target.install_data(data_folder=data_folder)
            target.configure()
        except Exception as err:
            print(f"Failed to install: {err}")

    # Deactivate caffeine and exit
    deactivate_caffeine()
    exit(0)


if __name__ == "__main__":
    main()
