import logging

from .ArgsParser import ArgsParser
from .handlers.FeedCacher import FeedCacher
from .handlers.FeedReader import FeedReader
from .handlers.FeedFilter import FeedFilter
from .handlers.FeedFormatter import FeedFormatter
from .handlers.FeedWriter import FeedWriter
from .Chain import Chain

from .ExecutionParams import ExecutionParams


def main():
    args_parser = ArgsParser()
    chain = Chain(FeedCacher(FeedReader()),
                  FeedFilter(), FeedFormatter(), FeedWriter())

    args = args_parser.parse_args()
    params = ExecutionParams(
        args.source[0], args.json, args.date, args.limit)

    logging.basicConfig(level=args.log_level)

    chain.execute(params)


if __name__ == "__main__":
    main()
