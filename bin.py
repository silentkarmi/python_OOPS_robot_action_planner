#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

@dataclass
class Bin:
    id: int
    parts: list()
    type: str = None
    
    def __init__(self, id) -> None:
        self.id = id
    
    def get_part(self):
        if self.parts:
            return self.parts.pop()
    