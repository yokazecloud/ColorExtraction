from enum import IntEnum

class HUE(IntEnum):
    RED     = 0
    ORANGE  = 15
    YELLOW  = 30
    GREEN   = 60
    EMERALD = 75
    CYAN    = 90
    BLUE    = 120
    PURPLE  = 135
    MAGENTA = 150
    
    def value(color_name: str) -> int:
        for e in HUE:
            if e.name == color_name:
                return e