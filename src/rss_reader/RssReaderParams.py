import dataclasses
from datetime import date


@dataclasses.dataclass
class RssReaderParams:
    """Class for storing parameters of the RssReader util"""

    """Source URL of the feed"""
    source: str

    """Limit the number of feed entries to the specified number"""
    limit: int

    """Get feed from the specified publishing date. If specified,
    the feed will be loaded from the cache
    """
    date: date
