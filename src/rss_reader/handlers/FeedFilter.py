from .Handler import Handler
from ..ExecutionContext import ExecutionContext


class FeedFilter(Handler):
    def __init__(self):
        super().__init__(FeedFilter.__name__)

    def handle(self, ctx: ExecutionContext) -> None:
        pass
