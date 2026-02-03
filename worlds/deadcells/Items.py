from enum import Enum
from typing import NamedTuple
from BaseClasses import Item, ItemClassification

class ItemGroup(str, Enum):
    RUNE = "Rune",
    SCROLL = "Scroll"
    MELEE = "Melee Weapon"
    KEY = "Key"