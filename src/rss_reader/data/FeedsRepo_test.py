import unittest
from unittest.mock import Mock, sentinel

from datetime import datetime
from tinydb import Query

from .FeedsRepo import FeedsRepo


class TestFeedsRepo(unittest.TestCase):

    def test_get_entries(self):
        db = Mock()
        table = Mock()

        table.search.return_value = []
        db.table.return_value = table

        repo = FeedsRepo(db=db)

        actual_result = repo.get_entries()

        self.assertEqual(actual_result, [])
        table.search.assert_called_once()

    def test_limt(self):
        db = Mock()
        table = Mock()

        table.search.return_value = [1, 2, 3, 4]
        db.table.return_value = table

        expected_limit = 2

        repo = FeedsRepo(db=db)

        actual_result = repo.get_entries(limit=expected_limit)

        self.assertEqual(len(actual_result), expected_limit)

    def test_query(self):
        db = Mock()
        table = Mock()

        table.search.return_value = []
        db.table.return_value = table

        FeedEntry = Query()
        timestamp = 1545730073
        date = datetime.fromtimestamp(timestamp)
        expected_query = (FeedEntry.link.exists()) & (
            FeedEntry.feed_link == sentinel.source) & (FeedEntry.published >= timestamp)

        repo = FeedsRepo(db=db)

        repo.get_entries(date=date, source=sentinel.source)

        table.search.assert_called_once_with(expected_query)


if __name__ == '__main__':
    unittest.main()
