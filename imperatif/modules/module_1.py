"""Exercices sur module_1.indtroduction"""

ZERO_TO_ONE_BASE_SHIFT: int = 1


def compute_sum_of_the_first_integers(upper_boundary):
    """Calculez la somme des premiers entiers"""
    if not isinstance(upper_boundary, int):
        raise TypeError("Provided value should be an int, received an {}".format(upper_boundary.__class__.__name__))

    if upper_boundary <= 0:
        result = 0
    else:
        result = int(upper_boundary * (upper_boundary + 1) / 2)

    return result


def print_sum_of_the_first_integers(upper_boundary):
    """À l'aide de la fonction print, affichez la somme des premiers entiers"""
    value = compute_sum_of_the_first_integers(upper_boundary)
    print(value)


def minmax(list_of_values):
    a = None
    b = None

    for v in list_of_values:
        a = v if a is None or v < a else a
        b = v if b is None or v > b else b

    return a, b