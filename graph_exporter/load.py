import os
import pickle
from collections import defaultdict
from enum import Enum
from typing import Any

import yaml
from yaml import FullLoader

from graph_exporter.typing import ImportData, GeoMixConfig


def load(root: str, method_name: str) -> list[ImportData]:
    class ImportType(Enum):
        MIXUP_ITEMS = 1
        METADATA = 2

    # ===
    # Parse files and create temporary dict.
    # ===

    temp_data: dict[str, dict[ImportType, Any]] = defaultdict(dict)
    for root, dirs, files in os.walk(root):
        for filename in files:
            timestamp, _ = filename.split("_")

            if filename.endswith(".pkl"):
                print(f"Importing {filename}")
                with open(os.path.join(root, filename), "rb") as f:
                    mixup_items = pickle.load(f)

                temp_data[timestamp][ImportType.MIXUP_ITEMS] = mixup_items

            elif filename.endswith(".yml"):
                print(f"Importing {filename}")
                with open(os.path.join(root, filename), "r") as f:
                    metadata = yaml.load(f, Loader=FullLoader)

                temp_data[timestamp][ImportType.METADATA] = metadata

    # ===
    # Convert into ImportData dict.
    # ===

    data: list[ImportData] = list()
    for item in temp_data.values():
        assert len(item) == 2, "Both mixup items and metadata must be present."

        metadata = item[ImportType.METADATA]

        if method_name == "geomix":
            metadata = GeoMixConfig(**metadata)
        else:
            raise TypeError(f"Unknown method {method_name}")

        data.append(
            ImportData(
                mixup_items=item[ImportType.MIXUP_ITEMS],
                metadata=metadata,
            )
        )

    return data
