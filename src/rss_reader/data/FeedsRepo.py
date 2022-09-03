import logging

from ..domain.Feed import Feed

from .FeedFilters import FeedFilters


class FeedsRepo:
    def __init__():
        pass

    def get_entries(filters: FeedFilters) -> Feed:
        """Gets the feed from the cache starting from the specified publishing
        date.

        Keyword arguments:
            filters: filters to be applied to the collection of feed entries

        Returns:
            feed entries from the cache
        """

        pass

    def upsert(feed: Feed):
        """Saves the feed to the cache

        Positional arguments:
            feed: feed to save
        """
        logging.info(f"Saving feed to cache")
        pass
