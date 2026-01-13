from enum import Enum

class ToonMode(str, Enum):
    LOSSLESS = "lossless"   # reversible
    LOSSY = "lossy"         # max compression