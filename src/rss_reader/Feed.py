from dataclasses import dataclass
from datetime import date


@dataclass
class Feed(object):
    """Representation of Feed."""

    title: str
    link: str
    sourse: str
