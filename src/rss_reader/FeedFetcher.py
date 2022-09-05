import feedparser

from .domain import Feed, FeedEntry


class FeedFetcher:
    """Fetches the feed from the specified source"""

    def __init__(self):
        pass

    def fetch(self, source: str) -> Feed:
        """Fetches the feed from the specified source.

        Keyword arguments:
            source: Source URL of the feed

        Returns:
            Requested feed
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

        feed = self._create_feed(response, source)

        return feed

    def _create_feed(self, response: dict, source: str) -> Feed:
        """Creates the feed from the response"""
        feed_response = response.feed
        return Feed(
            title=feed_response.title,
            link=source,
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
