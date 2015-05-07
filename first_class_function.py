#!/usr/bin/env python

import math


def hypo(x,y):
  return math.sqrt( (x*x) + (y*y) )

def circleArea(r):
  return math.pi*r*r

# result = math.trunc(hypo(3,4))
result = circleArea(3)
print(result)
