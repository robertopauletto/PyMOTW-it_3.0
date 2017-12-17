# argparse_long.py

import argparse

parser = argparse.ArgumentParser(
    description='Esempio con nomi di opzione lunghi',
)

parser.add_argument('--nessunargomento', action="store_true",
                    default=False)
parser.add_argument('--conargomenti', action="store",
                    dest="conargomenti")
parser.add_argument('--conargomenti2', action="store",
                    dest="conargomenti2", type=int)

print(
    parser.parse_args(
        ['--nessunargomento', '--conargomenti', 'val', '--conargomenti2=3']
    )
)
