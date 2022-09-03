import dataclasses
from datetime import date


@dataclasses.dataclass
class FeedFilters:
    """Class for storing filters for the feed entries"""
    source: str
    limit: int
    date: date
