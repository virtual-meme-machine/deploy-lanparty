import os
import shutil
import tempfile
import zipfile

from utils.file_utils import download_file

GOLDBERG_URL: str = "https://gitlab.com/Mr_Goldberg/goldberg_emulator/-/jobs/4247811310/artifacts/download"
STEAM_EMULATOR_DLL: str = None
STEAM_EMULATOR_X64_DLL: str = None


def download_steam_emulator():
    """
    Downloads Goldberg Emulator and extracts the emulated Steam API DLL files from it
    :return: None
    """
    temp_dir = tempfile.mkdtemp()
    download_path = os.path.join(temp_dir, "goldberg.zip")
    download_file(url=GOLDBERG_URL, output=download_path)

    with zipfile.ZipFile(file=download_path, mode="r") as zip_data:
        zip_data.extract(member="steam_api.dll", path=temp_dir)
        zip_data.extract(member="steam_api64.dll", path=temp_dir)

    global STEAM_EMULATOR_DLL
    global STEAM_EMULATOR_X64_DLL
    STEAM_EMULATOR_DLL = os.path.join(temp_dir, "steam_api.dll")
    STEAM_EMULATOR_X64_DLL = os.path.join(temp_dir, "steam_api64.dll")


def install_steam_emulator(target_directory: str, steam_app_id: int, x64: bool = False):
    """
    Installs and configures a Steam emulator in the provided target directory
    This disables Steam integration and allows LAN play without Steam running
    :param target_directory: Directory where the emulator should be installed
    :param steam_app_id: Steam app ID that the emulator should use
    :param x64: Boolean that denotes if we want the 32bit or 64bit Steam API DLL
    :return: None
    """
    steam_api_dll = os.path.join(target_directory, "steam_api64.dll" if x64 else "steam_api.dll")
    steam_api_dll_backup = f"{steam_api_dll}.backup"

    if os.path.isfile(path=steam_api_dll_backup):
        print(f"Steam emulator already installed")
        return

    print("Installing Steam emulator")
    if STEAM_EMULATOR_DLL is None or STEAM_EMULATOR_X64_DLL is None:
        download_steam_emulator()

    shutil.move(src=steam_api_dll, dst=steam_api_dll_backup)
    shutil.copy2(src=STEAM_EMULATOR_X64_DLL if x64 else STEAM_EMULATOR_DLL, dst=steam_api_dll)

    with open(file=os.path.join(target_directory, "steam_appid.txt"), mode="w") as steam_appid_file:
        steam_appid_file.write(str(steam_app_id))
