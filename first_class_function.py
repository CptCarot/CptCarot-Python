#!/usr/bin/env python

import math


def hypo(x,y):
  return math.sqrt( (x*x) + (y*y) )

result = math.trunc(hypo(3,4))
print(result)
