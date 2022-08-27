from dataclasses import dataclass

from .ExecutionArgs import ExecutionArgs
from .Feed import Feed


@dataclass
class ExecutionContext(object):
    """Class for keeping the context of the execution."""

    args: ExecutionArgs = None
    feed: list[Feed] = None
