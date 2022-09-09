from datetime import datetime
from .Formatter import Formatter


class Color:
    BOLD = '\033[1m'
    END = '\033[0m'


class DefaultFormatter(Formatter):
    "Formats the list of feed entries as a simple formatted string"

    def format(self, entries: list[dict]) -> None:
        "Prints the list of feed entries to the console"

        lines = ['\n']

        for entry in entries:
            lines.append(self._print_entry(entry))

        return '\n'.join(lines)

    def _print_entry(self, entry: dict) -> str:
        "Prints the feed entry"

        lines = []

        lines.append(self._print_attr("Title", entry.get('title')))
        lines.append(self._print_date_attr("Date", entry.get('published')))
        lines.append(self._print_attr("Link", entry.get('link')))

        if entry.get('description'):
            lines.append(entry.get('description'))

        return '\n'.join(lines)

    def _print_attr(self, name: str, attr: str) -> str:
        "Prints the attribute of the feed entry"

        return f"{Color.BOLD}{name}:{Color.END} {attr}"

    def _print_date_attr(self, name: str, timestamp: float) -> str:
        "Prints the date attribute of the feed entry"

        date = datetime.fromtimestamp(timestamp)
        return self._print_attr(name, date)
