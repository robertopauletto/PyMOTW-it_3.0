#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
    return ' %s:%s: %s:%s' % (filename, lineno, category.__name__, message)

warnings.warn('Messaggio di avvertimento, prima')
warnings.formatwarning = warning_on_one_line
warnings.warn('Messaggio di avvertimento, dopo')

