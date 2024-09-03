from sentiment_analysis.config.core import PACKAGE_ROOT


version_file_path = PACKAGE_ROOT / "VERSION"
with open(version_file_path, "r") as f:
    __version__ = f.read().strip()