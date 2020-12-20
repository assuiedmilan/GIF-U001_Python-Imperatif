import math

import pytest


def statistiques(list_of_values):

    if not list_of_values:
        return None
    elif len(list_of_values) == 1:
        return (list_of_values[0], 0)
    else:
        average = sum(x for x in list_of_values) / len(list_of_values)
        deviation = math.sqrt(1 / (len(list_of_values) - 1)
                              * sum((x - average) ** 2 for x in list_of_values))

    return average, deviation


@pytest.mark.parametrize("values, result",
                         [
                             ([1, 2, 3, 4, 5], (3.0, 1.5811388300841898)),
                             ([], None),
                             ([5], (5, 0))
                         ])
def test_statistiques(values, result):
    assert statistiques(values) == result
