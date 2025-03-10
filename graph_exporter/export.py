import sys
import pickle
import time
import os
from typing import Any

import yaml

from graph_exporter.typing import MixupItem


def export(
    mixup_items: list[MixupItem],
    dataset_name: str,
    metadata: dict[str, Any],
    *,
    base_dir: str = "export",
    terminate: bool = True,
) -> None:
    path = os.path.join(base_dir, dataset_name)
    os.makedirs(path, exist_ok=True)
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")

    with open(os.path.join(path, timestamp + "_graphs.pkl"), "wb") as f:
        pickle.dump(mixup_items, f)

    with open(os.path.join(path, timestamp + "_metadata.yml"), "w") as f:
        yaml.dump(metadata, f)

    if terminate:
        sys.exit(0)
