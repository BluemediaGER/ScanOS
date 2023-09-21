from enum import Enum

class Status(Enum):
    INITIALIZED = "initialized"
    IDLE = "idle"
    RUNNING = "running"
    DONE = "done"
    ERR_NO_PAPER = "err_no_paper"
    ERR_COVER_OPEN = "err_cover_open"

class Setting(Enum):
    PAPER_SOURCE = "source"
    COLOR_MODE = "color"
    RESOLUTION = "resolution"
    PAPER_SIZE = "paper_size"

class PaperSize(Enum):
    A3 = "a3"
    B3 = "b3"
    A4 = "a4"
    B4 = "b4"
    LETTER = "letter"