def palindrome(value):

    if isinstance(value, str):
        value = list(value)

    reversed_value = value.copy()
    reversed_value.reverse()

    return value == reversed_value


def test_palindrome():
    assert palindrome('anana')
    assert not palindrome('ananas')
