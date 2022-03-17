"""Assembly Station Class
"""
#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass

@dataclass
class AssemblyStation:
    """Assembly Station Class contains only id
    """
    # pylint: disable=invalid-name
    id : int
