import argparse
import datetime

from .Handler import Handler
from ..ExecutionContext import ExecutionContext
from ..ExecutionArgs import ExecutionArgs


class ArgsParser(Handler):
    def __init__(self):
        super().__init__(ArgsParser.__name__)

        parser = argparse.ArgumentParser(
            description='Pure Python command-line RSS reader.')

        parser.add_argument('source', type=str, nargs=1,
                            help='RSS URL')

        parser.add_argument('--version', help='Print version info',
                            action='version', version='%(prog)s 1.0')
        parser.add_argument(
            '--json', help='Print result as JSON in stdout', action='store_false')
        parser.add_argument(
            '--verbose', help='Outputs verbose status messages', action='store_false')
        parser.add_argument(
            '--limit', help='Limit news topics if this parameter provided')
        parser.add_argument('--date', help='Read articles starting from this date',
                            type=lambda s: datetime.datetime.strptime(s, '%Y%m%d'))

        self.parser = parser

    def handle(self, ctx: ExecutionContext) -> None:
        ctx.args = self._parse_args()

    """Parse CLI arguments and return ExecutionArgs object"""

    def _parse_args(self) -> argparse.Namespace:
        args = self.parser.parse_args()
        return ExecutionArgs(
            args.source, args.json, args.date, args.verbose, args.limit)
