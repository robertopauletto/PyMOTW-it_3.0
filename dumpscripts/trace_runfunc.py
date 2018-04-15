# trace_runfunc.py

import trace
from esempio_trace.recurse import recurse

tracer = trace.Trace(count=False, trace=True)
tracer.runfunc(recurse, 2)
