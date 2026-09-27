"""Small dependency-free progress bars for terminal and log output."""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import TextIO


@dataclass
class Progress:
    stream: TextIO = sys.stderr
    stages: dict[str, tuple[int, int]] = field(default_factory=dict)
    width: int = 20

    def set(self, stage: str, done: int, total: int) -> None:
        total = max(total, 1)
        done = min(max(done, 0), total)
        self.stages[stage] = (done, total)
        filled = round(self.width * done / total)
        bar = "█" * filled + "░" * (self.width - filled)
        self.stream.write(f"{stage:<14} [{bar}] {done}/{total}\n")
        self.stream.flush()
