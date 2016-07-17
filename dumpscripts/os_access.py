#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

print 'Verifica:', __file__
print 'Esiste:', os.access(__file__, os.F_OK)
print 'Leggibile:', os.access(__file__, os.R_OK)
print 'Scrivibile:', os.access(__file__, os.W_OK)
print 'Eseguibile:', os.access(__file__, os.X_OK)



