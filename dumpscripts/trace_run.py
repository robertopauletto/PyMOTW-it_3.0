# trace_run.py

import trace
from esempio_trace.recurse import recurse

tracer = trace.Trace(count=False, trace=True)
tracer.run('recurse(2)')
