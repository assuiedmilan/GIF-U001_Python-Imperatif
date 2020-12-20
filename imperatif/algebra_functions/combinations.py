from itertools import product


def compute_all_combinations_of_positive_negative(*argv):
    return list(product(*((k, -k) for k in argv)))
