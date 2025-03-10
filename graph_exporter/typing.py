from dataclasses import dataclass
from typing import Any, Literal


# ===
# Method Configs.
# ===


@dataclass
class BaseConfig:
    seed: int


# ===
# GeoMix.
# ===


@dataclass
class GeoMixConfig(BaseConfig):
    num_graphs: int  # default: 10
    num_nodes: int  # default: 20
    alpha_fgw: float  # default: 1.0
    sample_dist: Literal["uniform", "beta"]  # default: uniform
    beta_alpha: float  # default: 5.0
    beta_beta: float  # default: 0.5
    uniform_min: float  # default: 0.0
    uniform_max: float  # default: 5e-2
    clip_eps: float  # default: 1e-3


# ===
# Import / Export.
# ===


@dataclass
class MixupItem:
    graph_dict: dict[str, Any]
    lam: float
    source_indices: tuple[int, int]


@dataclass
class ImportData:
    mixup_items: list[MixupItem]
    config: BaseConfig


