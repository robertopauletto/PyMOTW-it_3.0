# codecs_invertcaps.py

import string


def invertcaps(text):
    """Ritorna una nuova stringa con le maiuscole in minuscole e viceversa
    """
    return ''.join(
        c.upper() if c in string.ascii_lowercase
        else c.lower() if c in string.ascii_uppercase
        else c
        for c in text
    )


if __name__ == '__main__':
    print(invertcaps('ABCdef'))
    print(invertcaps('abcDEF'))
