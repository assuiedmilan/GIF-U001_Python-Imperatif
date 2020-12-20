import pytest

from containers_functions.converters import iterable2tuple


@pytest.mark.parametrize("value, expected_result", [
    ("Toto", ('T', 'o', 't','o')),
    ([i for i in range(-2, 5)], (-2, -1, 0, 1, 2, 3, 4)),
])
def test_iterable2tuple(value, expected_result):
    result = iterable2tuple(value)

    assert result == expected_result
    assert isinstance(result, tuple)
