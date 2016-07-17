#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def throws_global_name_error():
    print unknown_global_name

def throws_unbound_local():
    local_val = local_val + 1
    print local_val

try:
    throws_global_name_error()
except NameError, err:
    print 'Errore di nome globale:', err

try:
    throws_unbound_local()
except UnboundLocalError, err:
    print 'Errore di nome locale:', err
