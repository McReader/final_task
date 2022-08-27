from .Handler import Handler
from ..ExecutionContext import ExecutionContext


class FeedWriter(Handler):
    def __init__(self):
        super().__init__(FeedWriter.__name__)

    def handle(self, ctx: ExecutionContext) -> None:
        pass
