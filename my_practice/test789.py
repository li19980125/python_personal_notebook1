# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:25:31 2020

@author: li19980125
"""

import sys
f = [x for x in range(1,10)]
print(f)
f = [x+y for x in 'ABCDE' for y in '1234567']
print(f)

f = [x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f,))
print(f)
f = (x ** 2 for x in range(1,1000) )
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)


