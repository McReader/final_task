import logging

from rss_reader import RssReader

from .ArgsParser import ArgsParser

from .printer.DefaultPrinter import DefaultPrinter
from .printer.JsonPrinter import JsonPrinter


def main():
    params = ArgsParser().parse_args()

    if params.json:
        printer = JsonPrinter()
    else:
        printer = DefaultPrinter()

    logging.basicConfig(level=params.log_level)

    feed_entries = RssReader().read(params)

    printer.print(feed_entries)


if __name__ == "__main__":
    main()
