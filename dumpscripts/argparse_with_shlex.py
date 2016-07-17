#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
from ConfigParser import ConfigParser
import shlex

parser = argparse.ArgumentParser(description='Breve applicazione di esempio')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

config = ConfigParser()
config.read('argparse_witH_shlex.ini')
config_value = config.get('cli', 'options')
print 'Config  :', config_value

argument_list = shlex.split(config_value)
print 'Elenco param.:', argument_list

print 'Risultati :', parser.parse_args(argument_list)