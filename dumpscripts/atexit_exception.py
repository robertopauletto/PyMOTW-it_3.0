#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import atexit

def exit_with_exception(message):
    raise RuntimeError(message)

atexit.register(exit_with_exception, 'Registrata per prima')
atexit.register(exit_with_exception, 'Registrata per seconda')