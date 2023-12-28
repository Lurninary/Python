from date_check import is_past_date
import pytest
import datetime


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (datetime.date.today(), False),  # Сегодняшняя дата
        (datetime.date.today() + datetime.timedelta(days=7), False),  # Будущая дата
        (datetime.date.today() - datetime.timedelta(days=7), True),   # Прошедшая дата
    ],
)
def test_is_past_date(test_input, expected):
    assert is_past_date(test_input) == expected