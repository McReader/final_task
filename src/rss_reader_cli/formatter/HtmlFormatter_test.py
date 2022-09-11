import unittest
from tinydb.table import Document

from .HtmlFormatter import HtmlFormatter


class HtmlFormatterTest(unittest.TestCase):

    def test_format(self):
        document = Document({
            "title": "TestTitle",
            "published": 1234567890,
            "link": "https://test.com",
            "description": "TestDescription"
        }, doc_id=1)

        actual_result = HtmlFormatter().format([document])

        self.assertIn("TestTitle", actual_result)
        self.assertIn("https://test.com", actual_result)


if __name__ == '__main__':
    unittest.main()
