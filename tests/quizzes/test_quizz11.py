alphabet_morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',  '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}


def text2morse(value):

    def __convert_word(value):
        return ' '.join([alphabet_morse[x.upper()]for x in value])

    list_of_words = value.split()

    return ' | '.join([__convert_word(x) for x in list_of_words])

def test_test2morse():
    assert text2morse('python en morse') == '.--. -.-- - .... --- -. | . -. | -- --- .-. ... .'
