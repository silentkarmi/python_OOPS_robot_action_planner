#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from utility import print_error

@dataclass
class Bin:
    id: int
    parts: list()
    type: str = None
    
    def __init__(self, id) -> None:
        self.id = id
        self.parts = []
    
    def get_part(self):
        part = None
        if self.parts:
            part = self.parts.pop()
            
            # if list empty we change the bin type to None
            # now, it can store any part type
            if not self.parts:
                self.type = None
        
        return part
            
    def store_parts(self, parts):
        success = False
        if not self.parts and parts:
            self.type = parts[0].type
            
        if self.type == parts[0].type:
            if (len(self.parts) + len(parts) > 3 and 
                len(self.parts) + len(parts) < 10):
                self.parts.extend(parts)
                success = True
            else:
                print_error("Alteast 4 parts are stored, but not more than 9")
        else:
            print_error("This part type can't be stored with parts of other type in the same bin.")
        
        return success
    
    def __str__(self) -> str:
        return f"Bin(id={str(self.id)}, part_type={self.type})"
    