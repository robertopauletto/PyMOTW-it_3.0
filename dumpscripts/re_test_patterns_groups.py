# re_test_patterns_groups.py

import re

def test_patterns(text, patterns=[]):
    """Dato un testo sorgente ed un elenco di modelli
    cerca corrispondenze per ogni modello all'interno del testo
    e le stampa su stdout.
    """
    # Cerca ciascun modello nel testo e stampa i risultati
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print('  {!r}'.format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print(
                '  {}{!r}{} '.format(prefix,
                                     text[s:e],
                                     ' ' * (len(text) - e)),
                end=' ',
            )
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(
                    ' ' * (len(text) - s),
                    match.groupdict()),
                )
        print()
    return

