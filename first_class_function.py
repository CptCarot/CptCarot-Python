#!/usr/bin/env python

import math


def hypo(x,y):
  return math.sqrt( (x*x) + (y*y) )

def circleArea(r):
  return math.pi*r*r

def circleCirc(r):
  return math.pi*2*r

# result = math.trunc(hypo(3,4))
# result = circleArea(3)
result = circleCirc(3)
print(   str(result)   )
