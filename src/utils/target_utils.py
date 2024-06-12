import importlib.util
import inspect
import os
import sys

from data.InstallTarget import InstallTarget


def load_targets(target_folder: str) -> list[InstallTarget]:
    """
    Loads a list of InstallTarget objects from raw class files
    :param target_folder: Directory containing class files
    :return: List of InstallTarget objects
    """
    targets: list[InstallTarget] = []

    for target_file in os.listdir(target_folder):
        if os.path.splitext(target_file)[1] != ".py":
            continue

        target_name = os.path.splitext(target_file)[0]
        module_name = f"target.{target_name}"
        target_file_path = os.path.join(target_folder, f"{target_name}.py")

        spec = importlib.util.spec_from_file_location(module_name, target_file_path)
        module = importlib.util.module_from_spec(spec)

        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        for name, obj in inspect.getmembers(sys.modules[module_name]):
            if name == target_name and inspect.isclass(obj) and issubclass(obj.__class__, InstallTarget.__class__):
                targets.append(obj())

    return sorted(targets, key=lambda target: target.name.lower())
