def palindrome(value):

    if isinstance(value, str):
        value = [x for x in value]

    reversed = value.copy()
    reversed.reverse()

    return value == value.copy().reverse()


def test_palindrome():
    assert palindrome('anana')
    assert not palindrome('ananas')