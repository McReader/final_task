from dataclasses import dataclass

from .ExecutionParams import ExecutionParams
from .Feed import Feed


@dataclass
class ExecutionContext(object):
    """Class for keeping the context of the execution."""

    args: ExecutionParams = None
    feed: list[Feed] = None
