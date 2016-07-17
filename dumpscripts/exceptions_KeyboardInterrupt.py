#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    print 'Premere Invio o Ctrl-C:',
    ignored = raw_input()
except Exception, err:
    print 'Eccepezione catturata:', err
except KeyboardInterrupt, err:
    print 'Catturato KeyboardInterrupt'
else:
    print 'Nessuna eccezione'
