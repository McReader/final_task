import feedparser

from .Handler import Handler
from ..ExecutionContext import ExecutionContext


class FeedReader(Handler):
    """A link of the chain responsible for the feed download"""

    def __init__(self):
        super().__init__(FeedReader.__name__)

    def handle(self, ctx: ExecutionContext) -> None:
        """Handles the feed download operation from the "source" specified by user.

        Keyword arguments:
            ctx: execution context of the entire chain
        """
        try:
            response = feedparser.parse(ctx.args.source)
            if response.bozo:
                raise response.bozo_exception
        except (feedparser.CharacterEncodingUnknown, feedparser.CharacterEncodingOverride) as e:
            raise Exception("The feed has incorrectly-declared encodings")
        except feedparser.NonXMLContentType as e:
            raise Exception("The feed is not XML")
        except Exception as e:
            raise Exception(f"Failed to read feed due to unknown error: {e}")

        ctx.feed = response.feed
