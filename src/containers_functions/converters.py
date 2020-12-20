def bin2int(binary_string):
    result = 0
    list_of_binary_items = [int(value) for value in list(binary_string)]

    for index, value in enumerate(reversed(list_of_binary_items)):
        result += value * pow(2, index)

    return result


def iterable2tuple(iterable):
    return tuple(iterable)
