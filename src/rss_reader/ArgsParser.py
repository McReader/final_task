import argparse
import logging
import datetime

from .ExecutionParams import ExecutionParams


class ArgsParser:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Pure Python command-line RSS reader.')

        parser.add_argument('source', type=str, nargs=1,
                            help='RSS URL')

        parser.add_argument('--version', help='Print version info',
                            action='version', version='%(prog)s 1.0')
        parser.add_argument(
            '--json', help='Print result as JSON in stdout', action='store_false')
        parser.add_argument(
            '--verbose', help='Outputs verbose status messages', action="store_const", dest="log_level", const=logging.INFO)
        parser.add_argument(
            '--limit', help='Limit news topics if this parameter provided')
        parser.add_argument('--date', help='Read articles starting from this date',
                            type=lambda s: datetime.datetime.strptime(s, '%Y%m%d'))

        self.parser = parser

    """Parse CLI arguments and return ExecutionArgs object"""

    def parse_args(self) -> ExecutionParams:
        args = self.parser.parse_args()
        params = ExecutionParams(
            args.source[0], args.json, args.date, args.limit)
        return params
