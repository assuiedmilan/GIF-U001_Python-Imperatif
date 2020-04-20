def compute_sum_of_the_first_integers(upper_boundary):

    numbers = range(upper_boundary)

    result = 0
    for number in numbers:
        result = result + number

    return result

def print_sum_of_the_first_integers(upper_boundary):

    value = compute_sum_of_the_first_integers(upper_boundary)
    print(value)