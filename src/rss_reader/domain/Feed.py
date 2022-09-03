from dataclasses import dataclass
from datetime import date

from .FeedEntry import FeedEntry


@dataclass
class Feed(object):
    """Feed domain model"""

    title: str
    link: str
    description: str
    published: date
    entries: list[FeedEntry] = []
