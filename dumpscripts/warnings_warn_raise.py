#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

warnings.simplefilter('error', UserWarning)

print "Prima dell'avvertimento"
warnings.warn('Questo è un messaggio di avvertimento')
print "Dopo l'avvertimento"
