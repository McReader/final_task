from tinydb import TinyDB, Query
import datetime
from time import mktime

from ..domain import Feed


class FeedsRepo:
    """Repository for the feeds"""

    def __init__(self, db: TinyDB = TinyDB("db.json")):
        self.table = db.table("entries")

    def get_all(self, date: datetime.date, limit: int) -> list[Feed]:
        """Gets the feed from the cache starting from the specified publishing
        date.

        Keyword arguments:
            date: publishing date to start from
            limit: number of entries to return

        Returns:
            feeds from the cache
        """

        docs = self.table.search()

        return self._limit(docs, limit)

    def get_by_source(self, source: str, date: datetime.date, limit: int) -> Feed:
        """Gets the feed from the cache starting from the specified publishing
        date.

        Keyword arguments:
            source: feed source to filter by
            date: publishing date to start from
            limit: number of entries to return

        Returns:
            feeds from the cache
        """

        docs = self.table.search(Query().feed_link == source)

        return self._limit(docs, limit)

    def upsert(self, feed: Feed):
        """Saves the feed to the cache

        Positional arguments:
            feed: feed to save
        """

        self._remove_feed_entries(feed)
        self._insert_feed_entries(feed)

    def _remove_feed_entries(self, feed: Feed):
        """Removes feed's entries from the cache

        Positional arguments:
            feed: feed to remove entries from
        """

        query = Query().feed_link == feed.link
        self.table.remove(query)

    def _insert_feed_entries(self, feed: Feed):
        """Inserts feed's entries to the cache

        Positional arguments:
            feed: feed to insert entries to
        """
        docs = []

        for entry in feed.entries:
            doc = {
                "feed_link": feed.link,
                "feed_title": feed.title,
                "id": entry.id,
                "title": entry.title,
                "link": entry.link,
                "description": entry.description,
                "published": mktime(entry.published),
            }
            docs.append(doc)

        self.table.insert_multiple(docs)

    def _limit(self, list: list, limit: int) -> list:
        """Limits the list to the specified number of items

        Positional arguments:
            list: list to limit
            limit: number of items to return

        Returns:
            limited list
        """

        return list[:limit]
