from .RssReaderParams import RssReaderParams
from .FeedFetcher import FeedFetcher

from .domain import Feed, FeedEntry
from .data import FeedsRepo, FeedFilters


class RssReader:
    """Downloads the feed from the source"""

    def __init__(self, fetcher: FeedFetcher, repo: FeedsRepo):
        self.fetcher = fetcher
        self.repo = repo

    def read_entries(self, params: RssReaderParams) -> list[FeedEntry]:
        """Loads the feed entries from the source specified by user and caches it. If the user
        specified the date filter, the feed will be loaded from the cache

        Positional arguments:
            params: RssReaderParams object containing the parameters of the util

        Returns:
            Array of feed entries
        """

        if self._is_sync_required(params):
            feed = self._load_from_source(params.source)
            self._persist_results(feed)

        return self._read_from_cache(params)

    def _is_sync_required(params: RssReaderParams) -> bool:
        """Determines if the feed should be loaded from the source"""
        is_date_filter_empty = params.date is None
        return is_date_filter_empty

    def _load_from_source(self, source: str) -> Feed:
        """Loads the feed from the source"""
        return self.fetcher.fetch(source)

    def _persist_results(self, feed: Feed) -> None:
        """Persists the feed to the cache"""
        self.repo.upsert(feed)

    def _read_from_cache(self, params: RssReaderParams) -> list[FeedEntry]:
        """Reads the feed from the cache"""
        filters = FeedFilters(source=params.source,
                              limit=params.limit, date=params.date)
        return self.repo.get_entries(filters)
