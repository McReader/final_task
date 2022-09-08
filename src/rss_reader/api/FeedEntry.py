from dataclasses import dataclass
from datetime import date


@dataclass
class FeedEntry(object):
    """Feed entry domain model"""

    id: str
    title: str
    link: str
    description: str
    published: date
