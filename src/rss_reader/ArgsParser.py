import argparse
import logging
import datetime

from .RssReaderArgs import RssReaderArgs


class ArgsParser:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Pure Python command-line RSS reader.')

        parser.add_argument('source', type=str,
                            help='RSS URL', nargs='?', default=None)

        parser.add_argument('--version', help='Print version info',
                            action='version', version='%(prog)s 1.1')
        parser.add_argument(
            '--json', help='Print result as JSON in stdout', action='store_true')
        parser.add_argument(
            '--verbose', help='Outputs verbose status messages', action="store_const", dest="log_level", const=logging.INFO)
        parser.add_argument(
            '--limit', help='Limit news topics if this parameter provided', type=int)
        parser.add_argument('--date', help='Read articles starting from this date',
                            type=lambda s: datetime.datetime.strptime(s, '%Y%m%d'))

        self.parser = parser

    """Parse CLI arguments and return ExecutionArgs object"""

    def parse_args(self) -> RssReaderArgs:
        args = self.parser.parse_args()
        params = RssReaderArgs(
            source=args.source, log_level=args.log_level, json=args.json, date=args.date, limit=args.limit)

        if not params.source and not params.date:
            self.parser.error(
                'the following arguments are required: source or --date')

        return params
