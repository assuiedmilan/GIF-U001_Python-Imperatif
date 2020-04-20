import pytest

from algebra.suites_operations import compute_sum_of_the_first_integers, print_sum_of_the_first_integers

@pytest.mark.parametrize("integer_to_test, expected_results", [(9, 45), (-5,0), (-1,0), (1, 1), (0,0), (100, 5050)])
def test_compute_sum_of_the_first_integers(integer_to_test, expected_results):
    assert compute_sum_of_the_first_integers(integer_to_test) == expected_results

@pytest.mark.parametrize("integer_to_test", [9.5, "9"])
def test_compute_sum_of_the_first_integers_invalid_entries(integer_to_test):
    with pytest.raises(TypeError):
        compute_sum_of_the_first_integers(integer_to_test)

@pytest.mark.parametrize("integer_to_test, expected_results", [(9, "45\n")])
def test_print_sum_of_the_first_integers(integer_to_test, expected_results, capsys):
    print_sum_of_the_first_integers(integer_to_test)
    capture_from_stdout = capsys.readouterr()
    assert capture_from_stdout.out == expected_results

@pytest.mark.parametrize("integer_to_test", [9.5, "9"])
def test_print_sum_of_the_first_integers_invalid_entries(integer_to_test):
    with pytest.raises(TypeError):
        print_sum_of_the_first_integers(integer_to_test)