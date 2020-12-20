import pytest
from imperatif.algebra_functions.operations import minmax

from imperatif.algebra_functions.operations import print_sum_of_the_first_integers

from imperatif.algebra_functions.operations import compute_sum_of_the_first_integers


@pytest.mark.parametrize("integer_to_test, expected_results", [(9, 45), (-5, 0), (-1, 0), (1, 1), (0, 0), (100, 5050)])
def test_compute_sum_of_the_first_integers(integer_to_test, expected_results):
    assert compute_sum_of_the_first_integers(integer_to_test) == expected_results


@pytest.mark.parametrize("upper_bound, class_received", [(9.5, "float"), ("9", "str")])
def test_compute_sum_of_the_first_integers_invalid_inputs(upper_bound, class_received):
    with pytest.raises(TypeError) as execution_info:
        compute_sum_of_the_first_integers(upper_bound)

    assert "Provided value should be an int, received an {}".format(class_received) in str(execution_info.value)


@pytest.mark.parametrize("integer_to_test, expected_results", [(9, "45\n")])
def test_print_sum_of_the_first_integers(integer_to_test, expected_results, capsys):
    print_sum_of_the_first_integers(integer_to_test)
    capture_from_stdout = capsys.readouterr()
    assert capture_from_stdout.out == expected_results


@pytest.mark.parametrize("upper_bound, class_received", [(9.5, "float"), ("9", "str")])
def test_print_sum_of_the_first_integer_invalid_inputs(upper_bound, class_received):
    with pytest.raises(TypeError) as execution_info:
        print_sum_of_the_first_integers(upper_bound)

    assert "Provided value should be an int, received an {}".format(class_received) in str(execution_info.value)


@pytest.mark.parametrize("values, expected_results", [
    ([-1, 3, 5, -2, 15, 2, -5], (-5, 15))
])
def test_minmax(values, expected_results):
    assert expected_results == minmax(values)
