from enum import Enum


class ColorScheme(Enum):
    TRIAD_COLOR = "triadColor"
    SPLIT_COMPLEMENTARY_COLOR = "splitComplementaryColor"
    DYAD_COLOR = "dyadColor"
    TETRADE_COLOR = "tetradeColor"
    PENTAD_COLOR = "pentadColor"
    PENTAD_BKW_COLOR = "pentadBkwColor"
    HEXAD_COLOR = "hexadColor"
    HEXAD_BKW_COLOR = "hexadBkwColor"
    DOMINANT_COLOR = "dominantColor"
    ANALOGY_COLOR = "analogyColor"
    INTERMEDIATE_COLOR = "intermediateColor"
    DOMINANT_TONE = "dominantTone"
    INIT = "init"
    ERROR = "error"
