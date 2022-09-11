from ast import For
import unittest

from .Format import Format

from .HtmlFormatter import HtmlFormatter
from .Fb2Formatter import Fb2Formatter
from .JsonFormatter import JsonFormatter
from .DefaultFormatter import DefaultFormatter

from .get_formatter import get_formatter


class GetFormatterTest(unittest.TestCase):

    def test_default(self):
        instance = get_formatter()

        self.assertIsInstance(instance, DefaultFormatter)

    def test_html(self):
        instance = get_formatter(Format.HTML)

        self.assertIsInstance(instance, HtmlFormatter)

    def test_fb2(self):
        instance = get_formatter(Format.FB2)

        self.assertIsInstance(instance, Fb2Formatter)

    def test_json(self):
        instance = get_formatter(Format.JSON)

        self.assertIsInstance(instance, JsonFormatter)


if __name__ == '__main__':
    unittest.main()
