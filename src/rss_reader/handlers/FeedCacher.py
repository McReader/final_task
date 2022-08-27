from .Handler import Handler
from ..ExecutionContext import ExecutionContext


class FeedCacher(Handler):
    def __init__(self, next_handler: Handler):
        super().__init__(FeedCacher.__name__)
        self.next_handler = next_handler

    def handle(self, ctx: ExecutionContext) -> None:
        self.next_handler.handle(ctx)
