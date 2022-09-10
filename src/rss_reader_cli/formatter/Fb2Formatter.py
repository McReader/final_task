
from FB2 import FictionBook2

from .Formatter import Formatter


class Fb2Formatter(Formatter):
    "Formats the list of feed entries as a simple formatted string"

    def format(self, entries: list[dict]) -> str:
        book = FictionBook2()

        book.titleInfo.title = "News Feed"
        book.titleInfo.annotation = "The latest news"

        book.chapters = []

        for entry in entries:
            book.chapters.append(
                (entry.get('title'), [entry.get('description') or "", entry.get('link')]))

        return str(book)
