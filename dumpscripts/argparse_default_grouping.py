#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')

parser.add_argument('-a', action="store")
parser.add_argument('-b', action="store", help='Solo corta')
parser.add_argument('--long-b', '-b', action="store", help='Lunga e corta insieme')

print parser.parse_args(['-h'])