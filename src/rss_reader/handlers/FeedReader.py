from .Handler import Handler
from ..ExecutionContext import ExecutionContext


class FeedReader(Handler):
    def __init__(self):
        super().__init__(FeedReader.__name__)

    def handle(self, ctx: ExecutionContext) -> None:
        pass
