import json

from .Formatter import Formatter


class JsonFormatter(Formatter):
    """Format the feed entries as JSON"""

    def format(self, entries: list[dict]) -> str:
        """Format the feed entries as JSON"""

        return json.dumps(entries, indent=2)
