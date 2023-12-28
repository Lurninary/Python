import unittest
from unittest.mock import Mock, patch
from choice import choice_one


class TestChoiceOne(unittest.TestCase):
    @patch('random.choice', side_effect=lambda x: x[0])
    def test_choice_one_with_data(self, mock_choice):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [('Product1',), ('Product2',), ('Product3',)]
        result = choice_one(mock_cursor)

        self.assertIn(result, ['Product1', 'Product2', 'Product3'])

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_choice_one_empty_data(self, mock_choice):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []

        with self.assertRaises(IndexError):
            result = choice_one(mock_cursor)

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_choice_one_single_data(self, mock_choice):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [('SingleProduct',)]
        result = choice_one(mock_cursor)

        self.assertEqual(result, 'SingleProduct')


if __name__ == '__main__':
    unittest.main()