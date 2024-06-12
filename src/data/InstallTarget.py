import abc
import dataclasses
import os
import shutil
import zipfile


@dataclasses.dataclass
class InstallTarget(abc.ABC):
    """
    Object that contains data for a single installation target, such as a program or game
    """
    name: str
    description: str
    identifier: str
    requires_additional_data: bool
    additional_data_file: str or None
    target_root: str

    @abc.abstractmethod
    def configure(self):
        """
        Configures the target
        :return: None
        """
        raise NotImplemented

    @abc.abstractmethod
    def install(self):
        """
        Installs the target
        :return: None
        """
        raise NotImplemented

    def install_data(self, data_folder: str):
        """
        Extracts data from a provided additional data file
        :param data_folder: Directory containing user provided additional data files
        :return: None
        """
        if not self.additional_data_file:
            return

        source_data_file = os.path.join(data_folder, self.additional_data_file)
        target_data_file = os.path.join(self.target_root, os.path.basename(self.additional_data_file))

        if os.path.exists(path=target_data_file):
            print(f"Additional data already exists")
            return

        if not os.path.isfile(path=source_data_file) or not zipfile.is_zipfile(filename=source_data_file):
            raise FileNotFoundError(f"Provided data file {source_data_file} is not a valid zip file")

        print("Installing additional data from provided zip file")
        os.makedirs(name=self.target_root, exist_ok=True)
        shutil.copy2(src=source_data_file, dst=target_data_file)
        with zipfile.ZipFile(file=target_data_file, mode="r") as data_zip:
            data_zip.extractall(path=self.target_root)

    def move_game_data(self, source_paths: list[str], target_path: str, check_path: str):
        """
        Moves game data around in the target root
        :param source_paths: List of paths that should be copied to the target
        :param target_path: Path to the source paths should be copied to
        :param check_path: Path that should be used to check if the game data already exists
        :return: None
        """
        for path in source_paths + [target_path, check_path]:
            if self.target_root not in path:
                print(f"{path} is not in the target root, game data will not be moved")
                return

        if os.path.isfile(path=check_path) or (os.path.isdir(s=check_path) and os.listdir(path=check_path)):
            print("Game data already exists")
            return

        print(f"Moving game data to {target_path}")
        os.makedirs(name=target_path, exist_ok=True)
        for source_path in source_paths:
            shutil.move(src=source_path, dst=target_path)
