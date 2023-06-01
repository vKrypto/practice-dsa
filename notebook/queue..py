import inspect
from dataclasses import dataclass, field
from typing import Any, List

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)