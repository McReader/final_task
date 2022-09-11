from dataclasses import dataclass
from datetime import date


@dataclass
class RssReaderParams:
    """Class for storing parameters of the RssReader util"""

    """Source URL of the feed"""
    source: str = None

    """Limit the number of feed entries to the specified number"""
    limit: int = None

    """Get feed from the specified publishing date. If specified,
    the feed will be loaded from the cache
    """
    date: date = None
