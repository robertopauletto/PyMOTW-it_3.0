#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import getopt

print getopt.getopt([ '--noarg', '--witharg', 'val', '--witharg2=another' ],
                    '',
                    [ 'noarg', 'witharg=', 'witharg2=' ])