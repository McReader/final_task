import unittest
from unittest.mock import Mock, sentinel

from feedparser import CharacterEncodingUnknown, NonXMLContentType

from ..exceptions import EncodingException, NonXmlTypeException

from .Api import Api


class TestApi(unittest.TestCase):

    def test_encoding_exception(self):
        parse = Mock(side_effect=CharacterEncodingUnknown)

        api = Api(parse=parse)

        with self.assertRaises(EncodingException):
            api.fetch_feed(sentinel.source)

    def test_non_xml_type_exception(self):
        parse = Mock(side_effect=NonXMLContentType)

        api = Api(parse=parse)

        with self.assertRaises(NonXmlTypeException):
            api.fetch_feed(sentinel.source)


if __name__ == '__main__':
    unittest.main()
