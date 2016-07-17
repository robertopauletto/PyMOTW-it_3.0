#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import trace
from trace_example.recurse import recurse


tracer = trace.Trace(count=False, trace=True)
tracer.run('recurse(2)')