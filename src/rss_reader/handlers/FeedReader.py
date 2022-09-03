import feedparser

from .Handler import Handler
from ..ExecutionContext import ExecutionContext
from ..domain import Feed, FeedEntry


class FeedReader(Handler):
    """A link of the chain responsible for the feed download"""

    def __init__(self):
        super().__init__(FeedReader.__name__)

    def handle(self, ctx: ExecutionContext):
        """Loads the feed from the "source" specified by user.

        Keyword arguments:
            ctx: execution context of the entire chain
        """
        feed = self.load(ctx.args.source)

        ctx.feed = feed

    def load(self, source: str) -> Feed:
        """Loads the feed from the "source" specified by user.

        Keyword arguments:
            source: feed source

        Returns:
            feed
        """
        try:
            response = feedparser.parse(source)
            if response.bozo:
                raise response.bozo_exception
        except (feedparser.CharacterEncodingUnknown, feedparser.CharacterEncodingOverride) as e:
            raise Exception("The feed has incorrectly-declared encodings")
        except feedparser.NonXMLContentType as e:
            raise Exception("The feed is not XML")
        except Exception:
            raise Exception(f"Failed to read feed due to unknown error")

        feed = self._create_feed(response)

        return feed

    def _create_feed(self, response: dict) -> Feed:
        """Creates the feed from the response"""
        feed_response = response.feed
        return Feed(
            title=feed_response.title,
            link=feed_response.link,
            description=feed_response.description,
            entries=self._create_entries(response.entries),
            published=feed_response.published_parsed
        )

    def _create_entries(self, entries: list) -> list:
        """Creates the feed entries from the response"""
        return [self._create_entry(entry) for entry in entries]

    def _create_entry(self, entry: dict) -> FeedEntry:
        """Creates the feed entry from the response"""
        return FeedEntry(
            id=entry.id,
            title=entry.title,
            link=entry.link,
            description="",
            published=entry.published_parsed
        )
