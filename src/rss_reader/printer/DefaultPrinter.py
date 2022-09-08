from tinydb import table


class color:
    BOLD = '\033[1m'
    END = '\033[0m'


class DefaultPrinter:
    "Prints the list of feed entries to the console"

    def print(self, entries: list[table.Document]) -> None:
        "Prints the list of feed entries to the console"

        print()

        for entry in entries:
            self._print_attr("Title", entry.get('title'))
            self._print_attr("Date", entry.get('published'))
            self._print_attr("Link", entry.get('link'))

            if entry.get('description'):
                print(entry.get('description'), end="\n")

            print()

    def _print_attr(self, name: str, attr: str) -> None:
        "Prints the attribute of the feed entry"

        print(f"{color.BOLD}{name}:{color.END} {attr}", end="\n\n")
