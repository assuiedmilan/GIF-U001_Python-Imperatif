def sapin(n):

    def compute_line(index):

        alignment = (n - index - 1) * ' '
        spacing = (index * ' -')[0:2 * index - 1]
        return '{}x'.format(alignment) + (index != 0) * '{}x'.format(spacing)

    if n < 0:
        raise AssertionError

    for x in range(n):
        yield compute_line(x)


def test_sapin():
    noel = sapin(10)
    print("\n".join(noel))