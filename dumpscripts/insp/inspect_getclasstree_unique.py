#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect
import example
from inspect_getclasstree import *

print_class_tree(inspect.getclasstree([example.A, example.B, C, D],
                                      unique=True,
                                      ))