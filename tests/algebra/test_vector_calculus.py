import pytest
from imperatif.algebra_functions.vector_calculus import compute_two_dimensional_norm

from imperatif.algebra_functions.combinations import compute_all_combinations_of_positive_negative


@pytest.mark.parametrize("x, y, expected_results", [(0, 0, 0), (1, 1, 1.414), (5, 9, 10.296)])
def test_compute_two_dimensional_norm(x, y, expected_results):
    combinations_of_positive_and_negative = compute_all_combinations_of_positive_negative(x, y)

    for values in combinations_of_positive_and_negative:
        result = round(compute_two_dimensional_norm(values[0], values[1]),3)
        assert result == expected_results
