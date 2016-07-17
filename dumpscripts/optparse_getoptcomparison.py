#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import optparse
import sys

print 'ARGV       :', sys.argv[1:]

parser = optparse.OptionParser()
parser.add_option('-o', '--output', 
                  dest="output_filename", 
                  default="default.out",
                  )
parser.add_option('-v', '--verbose',
                  dest="verbose",
                  default=False,
                  action="store_true",
                  )
parser.add_option('--version',
                  dest="version",
                  default=1.0,
                  type="float",
                  )
options, remainder = parser.parse_args()

print 'VERSIONE   :', options.version
print 'DETTAGLIATO:', options.verbose
print 'OUTPUT     :', options.output_filename
print 'RIMANENTI  :', remainder
