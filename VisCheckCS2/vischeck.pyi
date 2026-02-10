from dataclasses import dataclass
from typing import Sequence

@dataclass
class Vector3:
    x: float
    y: float
    z: float


class VisCheck:
    def __init__(self, file: str) -> None:
        ...

    def is_visible(self, point1: Sequence[tuple], point2: Sequence[tuple]) -> bool:
        ...

