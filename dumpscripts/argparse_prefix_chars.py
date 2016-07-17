#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Modifica i caratteri prefisso opzione',
                                 prefix_chars='-+/',
                                 )

parser.add_argument('-a', action="store_false", default=None,
                    help='Disattiva A',
                    )
parser.add_argument('+a', action="store_true", default=None,
                    help='Attiva A',
                    )
parser.add_argument('//noarg', '++noarg', action="store_true", default=False)

print parser.parse_args()