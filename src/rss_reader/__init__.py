import argparse

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


def main():
    args = parser.parse_args()
