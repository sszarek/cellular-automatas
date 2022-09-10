from dataclasses import dataclass

@dataclass(frozen=True)
class Configuration:
    """Represents configuraton of the Shell Application"""

    cell_size: int
    rows: int
    cols: int

    window_caption: str
    frame_rate: int
