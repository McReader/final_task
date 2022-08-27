from ..ExecutionContext import ExecutionContext


class Handler:
    "The interface that each Chain link must implement."

    def __init__(self, name: str):
        self.name = name

    "Handle the request and pass the result to the next link in the chain."

    def handle(self, ctx: ExecutionContext) -> None:
        pass
