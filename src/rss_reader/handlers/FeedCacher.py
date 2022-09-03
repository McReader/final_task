from ..ExecutionParams import ExecutionParams
from ..data.FeedRepo import FeedRepo

from .Handler import Handler


class FeedCacher(Handler):
    """A link of the chain responsible for the feed caching. Decorates the target handler with caching functionality"""

    def __init__(self, target: Handler, feed_repo: FeedRepo):
        super().__init__(FeedCacher.__name__)

        self.feed_repo = feed_repo
        self.target = target

    def handle(self, ctx: ExecutionParams) -> None:
        """Extracts feed from cache if --date argument was provided. Otherwise
        delegates the execution to the target handler and caches the result
        """
        date_filter = ctx.args.date
        if date_filter:
            ctx.feed = self._get_from_cache(ctx)
        else:
            self._call_target(ctx)

    def _get_from_cache(self, ctx: ExecutionContext) -> dict:
        """Gets the feed from the cache. Throws an exception 
        if the feed is not found
        """

        publishing_date = ctx.args.date
        source = ctx.args.source

        result = self.feed_repo.get_from_date(publishing_date, source=source)

        if not result:
            raise Exception("Failed to get feed from cache")

        return result

    def _call_target(self, ctx: ExecutionContext) -> None:
        """Calls the target handler and caches the result"""
        self.target.handle(ctx)
        self._cache_result(ctx)

    def _cache_result(self, ctx: ExecutionContext) -> None:
        """Caches the feed"""
        self.feed_repo.save(ctx.feed)
