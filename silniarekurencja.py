#!/usr/bin/env python

def silniareku(x):

    if x<2:
        return 1
    else:
        return x*silniareku(x-1)

print silniareku(4)
