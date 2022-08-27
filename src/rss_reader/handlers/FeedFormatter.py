from .Handler import Handler
from ..ExecutionContext import ExecutionContext


class FeedFormatter(Handler):
    def __init__(self):
        super().__init__(FeedFormatter.__name__)

    def handle(self, ctx: ExecutionContext) -> None:
        pass
