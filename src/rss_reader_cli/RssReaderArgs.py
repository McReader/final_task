import os
from dataclasses import dataclass, field
from datetime import date
import logging as logger

from .formatter.Format import Format


@dataclass
class RssReaderArgs(object):
    """Class for keeping the arguments of the execution."""

    source: str
    log_level: int = logger.WARN
    json: bool = False
    date: date = None
    limit: int = None
    to_html: str = None
    to_fb2: str = None

    output_file: str = field(init=False, default=None)
    output_file_format: Format = field(init=False, default=None)

    def __post_init__(self):
        """Post init hook"""

        if self.to_html:
            self.output_file = os.path.abspath(self.to_html)
            self.output_file_format = Format.HTML
        elif self.to_fb2:
            self.output_file = os.path.abspath(self.to_fb2)
            self.output_file_format = Format.FB2
