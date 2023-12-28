from date_check import is_past_date
import unittest
from unittest.mock import patch
import datetime


class TestIsPastDate(unittest.TestCase):
    @patch('date_check.is_past_date')
    def test_is_past_date_future_date(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime.date.today()
        future_date = datetime.date.today() + datetime.timedelta(days=7)
        result = is_past_date(future_date)  # False

        self.assertFalse(result, "Expected False for a future date")

    @patch('date_check.is_past_date')
    def test_is_past_date_past_date(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime.date.today()
        past_date = datetime.date.today() - datetime.timedelta(days=7)
        result = is_past_date(past_date)  # True

        self.assertTrue(result, "Expected True for a past date")

    @patch('date_check.is_past_date')
    def test_is_past_date_today(self, mock_datetime):
        mock_datetime.date.today.return_value = datetime.date.today()
        result = is_past_date(datetime.date.today())  # False

        self.assertFalse(result, "Expected False for today's date")


if __name__ == '__main__':
    unittest.main()