# math_inverse_trig.py

import math

for r in [0, 0.5, 1]:
    print('arcocoseno({:.1f})    = {:5.2f}'.format(r, math.asin(r)))
    print('arccoseno({:.1f})  = {:5.2f}'.format(r, math.acos(r)))
    print('arcotangente({:.1f}) = {:5.2f}'.format(r, math.atan(r)))
    print()
