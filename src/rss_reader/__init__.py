from .handlers.ArgsParser import ArgsParser
from .handlers.FeedCacher import FeedCacher
from .handlers.FeedReader import FeedReader
from .handlers.FeedFilter import FeedFilter
from .handlers.FeedFormatter import FeedFormatter
from .handlers.FeedWriter import FeedWriter
from .Chain import Chain


def main():
    chain = Chain(handlers=[ArgsParser(), FeedCacher(FeedReader()),
                  FeedFilter(), FeedFormatter(), FeedWriter()])

    chain.execute()


if __name__ == "__main__":
    main()
