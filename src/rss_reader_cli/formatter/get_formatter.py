from .Formatter import Formatter
from .HtmlFormatter import HtmlFormatter
from .JsonFormatter import JsonFormatter
from .DefaultFormatter import DefaultFormatter
from .Fb2Formatter import Fb2Formatter

from .Format import Format


def get_formatter(format: Format = None) -> Formatter:
    """Create the formatter for the target format"""
    if format == Format.HTML:
        return HtmlFormatter()
    elif format == Format.JSON:
        return JsonFormatter()
    elif format == Format.FB2:
        return Fb2Formatter()
    return DefaultFormatter()
