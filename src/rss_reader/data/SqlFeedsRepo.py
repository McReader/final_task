import sqlite3

from ..api.Feed import Feed
from ..definitions import CACHE_FILE


class SqlFeedsRepo:
    """Repository for the feeds"""

    SQL_CREATE_FEEDS_TABLE = """CREATE TABLE IF NOT EXISTS feeds (\
        link text PRIMARY KEY,\
        title text NOT NULL,\
    );"""

    SQL_CREATE_NEWS_TABLE = """CREATE TABLE IF NOT EXISTS news (\
        id text PRIMARY KEY,\
        title text NOT NULL,\
        link text NOT NULL,\
        description text,\
        published text,\
        feed_link text NOT NULL,\
        FOREIGN KEY (feed_link) REFERENCES feeds (link),\
    );"""

    def __init__(self, db_file = ":memory:"):
        self.db_file = db_file
        self._create_tables()

    def _get_connection(self):
        try:
            return sqlite3.connect(self.db_file)
        except Error as e:
            # todo handle database connection error
            raise e

    def _create_tables(self):
        con = self._get_connection()
        cur = con.cursor()

        try:
            cur.execute(SqlFeedsRepo.SQL_CREATE_FEEDS_TABLE)
            cur.execute(SqlFeedsRepo.SQL_CREATE_NEWS_TABLE)
        except Error as e:
            # todo handle error
            raise e
        finally:
            con.close()

    def get_entries(self, source: str = None, date: datetime.date = None, limit: int = None) -> list[dict]:
        """Gets the feed from the cache starting from the specified publishing
        date.

        Keyword arguments:
        source: feed source to filter by
        date: publishing date to start from
        limit: number of entries to return

        Returns:
        feeds from the cache
        """
        res = cur.execute("")

        pass

    def upsert(self, feed: Feed):
        """Saves the feed to the cache

        Positional arguments:
        feed: feed to save
        """
        pass

    def _remove_feed_entries(self, feed: Feed):
        """Removes feed's entries from the cache

        Positional arguments:
        feed: feed to remove entries from
        """

        pass

    def _insert_feed_entries(self, feed: Feed):
        """Inserts feed's entries to the cache

        Positional arguments:
        feed: feed to insert entries to
        """
        pass
