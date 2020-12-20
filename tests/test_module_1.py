import pytest

from imperatif.modules.module_1 import compute_sum_of_the_first_integers
from imperatif.modules.module_1 import print_sum_of_the_first_integers


@pytest.mark.parametrize("upper_bound, expected", [
    (9, 45), (100, 5050), (0, 0), (-1, 0),
    pytest.param((9.5, "float"), ("9", "str"), marks=pytest.mark.xfail(raises=TypeError))
])
def test_compute_sum_of_the_first_integers(upper_bound, expected):
    assert compute_sum_of_the_first_integers(upper_bound) == expected


@pytest.mark.parametrize("upper_bound, expected", [
    (9, "45\n"), (100, "5050\n"), (0, "0\n"), (-1, "0\n"),
    pytest.param((9.5, "float"), ("9", "str"), marks=pytest.mark.xfail(raises=TypeError))
])
def test_print_sum_of_the_first_integers(upper_bound, expected, capsys):
    print_sum_of_the_first_integers(upper_bound)
    capture_from_stdout = capsys.readouterr()
    assert capture_from_stdout.out == expected
