ZERO_TO_ONE_BASE_SHIFT = 1

def compute_sum_of_the_first_integers(upper_boundary):

    if not isinstance(upper_boundary, int):
        raise TypeError("Provided value should be an int, received an {}".format(upper_boundary.__class__.__name__))

    if upper_boundary <= 0:
        result = 0
    else:
        result = int(upper_boundary*(upper_boundary+1)/2)

    return result

def print_sum_of_the_first_integers(upper_boundary):

    value = compute_sum_of_the_first_integers(upper_boundary)
    print(value)