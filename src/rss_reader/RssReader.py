from .exceptions import NoFeedsFound
from .RssReaderParams import RssReaderParams
from .FeedFetcher import FeedFetcher

from .data import FeedsRepo
from .domain import Feed


class RssReader:
    """Downloads the feed from the source"""

    def __init__(self, fetcher: FeedFetcher = FeedFetcher(), repo: FeedsRepo = FeedsRepo()):
        self.fetcher = fetcher
        self.repo = repo

    def read(self, params: RssReaderParams) -> list[dict]:
        """Loads the feed entries from the source specified by user and caches it. If the user
        specified the date filter, the feed will be loaded from the cache

        Positional arguments:
            params: object containing the parameters of the util

        Returns:
            Array of feed entries
        """
        if not self._is_cache_only(params):
            feed = self._load_from_source(params.source)
            self._save_feed(feed)

        results = self._read_from_cache(params)

        if not results or len(results) == 0:
            raise NoFeedsFound()

        return results

    def _is_cache_only(self, params: RssReaderParams) -> bool:
        """Determines if the feed should be loaded from the source"""
        has_date_filter = params.date is not None
        return has_date_filter

    def _load_from_source(self, source: str) -> Feed:
        """Loads the feed from the source"""
        return self.fetcher.fetch(source)

    def _save_feed(self, feed: Feed) -> None:
        """Persists the feed to the cache"""
        self.repo.upsert(feed)

    def _read_from_cache(self, params: RssReaderParams) -> list[dict]:
        """Reads the feed from the cache"""

        return self.repo.get_entries(source=params.source, date=params.date, limit=params.limit)
