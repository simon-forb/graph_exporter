from dataclasses import dataclass
from typing import Any


@dataclass
class MixupItem:
    graph_dict: dict[str, Any]
    lam: float
    source_indices: tuple[int, int]


