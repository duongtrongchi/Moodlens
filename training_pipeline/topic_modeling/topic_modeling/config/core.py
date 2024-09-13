from pathlib import Path

import topic_modeling

PACKAGE_ROOT = Path(topic_modeling.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
DATASET_DIR = PACKAGE_ROOT / "datasets"

print(PACKAGE_ROOT)
print(ROOT)
print(DATASET_DIR)

