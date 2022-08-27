import logging

from .handlers.Handler import Handler
from .ExecutionContext import ExecutionContext


class Chain:
    def __init__(self, *handlers: list[Handler]):
        self.handlers = handlers

    def execute(self) -> None:
        ctx = ExecutionContext()

        for handler in self.handlers:
            logging.info(f"Executing handler {handler.name}")
            handler.handle(ctx=ctx)
            logging.info(f"Handler {handler.name} executed")
