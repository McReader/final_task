import logging

from .ArgsParser import ArgsParser
from .RssReader import RssReader


def main():
    args_parser = ArgsParser()
    rss_reader = RssReader()

    params = args_parser.parse_args()

    # logging.basicConfig(level=params.log_level)

    feed_entries = rss_reader.read(params)

    print(feed_entries)


if __name__ == "__main__":
    main()
