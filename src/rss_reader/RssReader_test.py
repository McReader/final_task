from os import access
import unittest
from unittest.mock import Mock, sentinel

from .RssReader import RssReader
from .RssReaderParams import RssReaderParams
from .exceptions import NoFeedsFound


class TestRssReader(unittest.TestCase):

    def test_read(self):
        api = Mock()
        repo = Mock()
        params = RssReaderParams(source=sentinel.source)
        expected_result = [sentinel.entry]

        api.fetch_feed.return_value = sentinel.feed
        repo.get_entries.return_value = expected_result

        reader = RssReader(api=api, repo=repo)
        actual_result = reader.read(params)

        self.assertEqual(actual_result, expected_result)
        api.fetch_feed.assert_called_once_with(params.source)
        repo.upsert.assert_called_once_with(sentinel.feed)

    def test_no_results(self):
        api = Mock()
        repo = Mock()
        params = RssReaderParams(source=sentinel.source)
        expected_result = []

        api.fetch_feed.return_value = sentinel.feed
        repo.get_entries.return_value = expected_result

        reader = RssReader(api=api, repo=repo)

        with self.assertRaises(NoFeedsFound):
            reader.read(params)

    def test_cache_only(self):
        api = Mock()
        repo = Mock()
        params = RssReaderParams(date=sentinel.date)
        expected_result = [sentinel.entry]

        repo.get_entries.return_value = expected_result

        reader = RssReader(api=api, repo=repo)
        actual_result = reader.read(params)

        self.assertEqual(actual_result, expected_result)
        api.fetch_feed.assert_not_called()
        repo.upsert.assert_not_called()


if __name__ == '__main__':
    unittest.main()
