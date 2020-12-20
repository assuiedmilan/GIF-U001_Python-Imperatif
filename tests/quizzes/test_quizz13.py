def palindrome(value):

    reversed_value = value.copy()
    reversed_value.reverse()

    return value == value.copy().reverse()


def test_palindrome():
    assert palindrome('anana')
    assert not palindrome('ananas')
