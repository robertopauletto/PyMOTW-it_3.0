# argparse_raw_description_help_formatter.py

import argparse

parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.RawTextHelpFormatter,
    description="""
    descrizione
        su piu'
           righe""",
    epilog="""
    conclusione
      su piu'
         righe""",
)

parser.add_argument(
    '-a', action="store_true",
    help="""argomento
    di aiuto non
    viene stampato su di una sola riga
    """,
)

parser.print_help()
