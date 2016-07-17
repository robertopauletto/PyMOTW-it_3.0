#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A, inspect.ismethod))