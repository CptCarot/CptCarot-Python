#!/usr/bin/env python


import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

def hypo(x,y):
  return math.sqrt( (x*x) + (y*y) )

def circleArea(r):
  return math.pi*r*r

def circleCirc(r):
  return math.pi*2*r

result1 = math.trunc(hypo(3,4))
result2 = circleArea(3)
result3 = circleCirc(3)

print( "          Hypotenuse = " + str(result1)   )
print( "         Circle Area = " + str(result2)   )
print( "Circle Circumference = " + str(result3)   )

# I added this while Merrick was with me
# My brother Mike is here with me.
