#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from typing import Any
from tray import Tray

from dataclasses import dataclass

@dataclass
class Table:
    tray: Any

    def get_tray(self):
        obj_tray = self.tray
        self.tray = None
        return obj_tray