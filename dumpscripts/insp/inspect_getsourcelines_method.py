#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect
import pprint
import example

pprint.pprint(inspect.getsourcelines(example.A.get_name))