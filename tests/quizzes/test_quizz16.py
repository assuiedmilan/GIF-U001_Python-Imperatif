

def losange(n):

    def compute_line(index):

        alignment = (n - index - 1) * ' '

        if index == 0:
            return '{}.'.format(alignment)

        number_of_spaces = (index - 1) * 2 + 1
        return '{}.{}.'.format(alignment, number_of_spaces * ' ')

    if n < 0:
        raise ValueError

    if n == 0:
        return

    top = [compute_line(x) for x in range(n)]
    bottom = top.copy()
    bottom.reverse()
    center = [compute_line(n)]

    print("\n".join(top + center + bottom))


def test_losange():
    losange(5)
