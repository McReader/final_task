from dataclasses import dataclass
from enum import Enum
from datetime import date
import logging as logger


class Format(Enum):
    """Enum of the all possible format converters"""

    JSON = 1


@dataclass
class RssReaderArgs(object):
    """Class for keeping the arguments of the execution."""

    source: str
    log_level: int = logger.WARN
    json: bool = False
    date: date = None
    limit: int = None
