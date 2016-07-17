#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import optparse

parser = optparse.OptionParser()
parser.add_option('--no-foo', action="store_true", 
                  default=False, 
                  dest="foo",
                  help="Disabilita foo",
                  )
parser.add_option('--with', action="store", help="Include caratteristiche opzionali")

parser.parse_args()
