#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings

def old_function():
    warnings.warn(
        'old_function() è deprecata, utilizzare new_function() al suo posto', 
        stacklevel=2)

def caller_of_old_function():
    old_function()
    
caller_of_old_function()