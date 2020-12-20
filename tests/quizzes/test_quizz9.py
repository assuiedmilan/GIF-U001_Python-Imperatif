def grille(m, n):
    if m <= 0 or n <= 0:
        return None

    line = ' ' + (n * 4 - 1) * '-' + '\n'
    column = (n) * '|   ' + '|\n'

    return ''.join([line if x % 2 == 0 else column for x in range(2 * m + 1)])


def test_grille():
    assert ' -----------\n|   |   |   |\n -----------\n|   |   |   |\n -----------\n' == grille(2, 3)
    assert ' ---------------\n|   |   |   |   |\n ---------------\n|   |   |   |   |\n ---------------\n|   |   |   |   |\n ---------------\n' == grille(
        3, 4)

    assert grille(0, 4) is None
    assert grille(-1, 4) is None
    assert grille(2, -1) is None
    assert grille(2, 0) is None
