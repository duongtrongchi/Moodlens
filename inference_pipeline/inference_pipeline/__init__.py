from inference_pipeline.config.core import PACKAGE_ROOT


VERSION_FILE_PATH = PACKAGE_ROOT / "VERSION"

with open(VERSION_FILE_PATH, "r") as f:
    __version__ = f.read().strip()

