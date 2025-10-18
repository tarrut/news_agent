import yaml
import os
from pathlib import Path

def load_config() -> dict[dict]:
    """Function for loading the configuration in .yml files

    Returns:
        Dictionary with the configuration specified inside the config fodler
    """

    config = {}

    base_path = Path("./config/")
    for file in os.listdir(base_path):
        filename = os.fsdecode(file)
        if filename.endswith(".yml"):
            file_path = base_path / filename
            config[filename.removesuffix(".yml")] = yaml.safe_load(open(file_path))
    
    return config