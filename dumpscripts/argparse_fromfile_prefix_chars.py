#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
from ConfigParser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='Breve applicazione di esempio',
                                 fromfile_prefix_chars='@',
                                 )

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print parser.parse_args(['@argparse_fromfile_prefix_chars.txt'])