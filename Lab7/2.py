import pytest


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@pytest.mark.parametrize("n, expected_result", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 50), # Падение теста
])
def test_fibonacci_sequence(n, expected_result):
    result = fib(n)
    assert result == expected_result, f"Error for n={n}: expected {expected_result}, got {result}"