#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser(description='Esempio con parametri non associati ad opzione')

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print parser.parse_args()
