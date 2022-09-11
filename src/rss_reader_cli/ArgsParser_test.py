import unittest

from .ArgsParser import ArgsParser


class ArgsParserTest(unittest.TestCase):

    def test_format(self):
        parser = ArgsParser()

        args = parser.parse_args(['https://news.yahoo.com/rss/'])

        self.assertEqual(args.source, 'https://news.yahoo.com/rss/')


if __name__ == '__main__':
    unittest.main()
