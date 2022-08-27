from rss_reader.ExecutionContext import ExecutionContext
from .handlers.Handler import Handler


class Chain:
    def __init__(self, handlers: list[Handler]):
        self.handlers = handlers

    def execute(self) -> None:
        ctx = ExecutionContext()

        for handler in self.handlers:
            print('Executing handler: {}'.format(handler.name))
            handler.handle(ctx=ctx)
            print('Handler executed: {}'.format(handler.name))
