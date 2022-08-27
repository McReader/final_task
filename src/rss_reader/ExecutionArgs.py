from dataclasses import dataclass
from enum import Enum
from datetime import date


class Format(Enum):
    """Enum of the all possible format converters"""

    JSON = 1


@dataclass
class ExecutionArgs(object):
    """Class for keeping the arguments of the execution."""

    source: str
    format: Format = None
    date: date = None
    verbose: bool = False
    limit: int = None
