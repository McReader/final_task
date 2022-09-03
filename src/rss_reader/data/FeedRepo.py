from datetime import date
import logging

from ..domain.Feed import Feed


class FeedRepo:
    def __init__():
        pass

    def get_entries(publishing_date: date, source: str, limit: int) -> Feed:
        """Gets the feed from the cache starting from the specified publishing
        date.

        Keyword arguments:
            publishing_date: date of the feed publishing (optional)
            source: feed source (optional)
            limit: number of entries to return (optional)

        Returns:
            feed entries from the cache
        """
        logging.info(
            f"Getting feed from cache for {publishing_date} and source {source}")
        pass

    def save(feed: Feed):
        """Saves the feed to the cache

        Positional arguments:
            feed: feed to save
        """
        logging.info(f"Saving feed to cache")
        pass
