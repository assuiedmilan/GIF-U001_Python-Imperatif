from algebra.combinations import compute_all_combinations_of_positive_negative


def test_two_values():
    result = compute_all_combinations_of_positive_negative(1, 2)

    assert (1,2) in result
    assert (1,-2) in result
    assert (-1,2) in result
    assert (-1,-2) in result


def test_three_values():
    result = compute_all_combinations_of_positive_negative(1, 2, 3)

    assert (1, 2, 3) in result
    assert (1, 2, -3) in result
    assert (1, -2, 3) in result
    assert (1, -2, -3) in result

    assert (-1, 2, 3) in result
    assert (-1, 2, -3) in result
    assert (-1, -2, 3) in result
    assert (-1, -2, -3) in result
