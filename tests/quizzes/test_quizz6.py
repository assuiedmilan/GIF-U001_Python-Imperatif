def foldingo(value):
    return ''.join(x.upper() if i % 2 == 0 else x.lower() for i, x in enumerate(value))


def test_foldingo():
    result = foldingo('bonjour')
    assert result == 'BoNjOuR'