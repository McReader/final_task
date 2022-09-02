import logging

from rss_reader.ExecutionParams import ExecutionParams

from .handlers.Handler import Handler
from .ExecutionContext import ExecutionContext


class Chain:
    """A chain of responsibility pattern implementation"""

    def __init__(self, *handlers: list[Handler]):
        self.handlers = handlers

    def execute(self, params: ExecutionParams) -> None:
        """Executes the chain of handlers"""
        ctx = ExecutionContext(args=params)

        for handler in self.handlers:
            logging.info(f"Executing handler {handler.name}")
            try:
                handler.handle(ctx=ctx)
            except Exception as e:
                logging.error(e)
                break
            logging.info(f"Handler {handler.name} executed")
