# This module generates triangles that have all integer sides and an angle
# of either 120 degrees or 60 degrees.
#
# To generate triangles with 120 degrees for each n = 1, 2, 3, ... find all
# the (i, j) such that ij = 3*n^2. The sides a and b adjacent to the 120
# degree angle will be a = i + 2*n and b = j + 2*n, c, the side opposite the
# 120 degree angle, will be c = i + j + 3*n.
#
# Each 120 degree traingle derives 2 60 degree triangles.
# For each 120 degree traingle (a, b, c) where a and b are are adjacent to the
# 120 degree angle and c is opposite, the corresponding 2 60 degree traingles
# are (a, a+b, c) and (b, a+b, c)


import itertools


def Triangles120():
  for n in itertools.count(1):
    for i, j in _Factors(3*n*n):
      yield i + 2*n, j + 2*n, i + j + 3*n


def Triangles60():
  for a, b, c in Triangles120():
    yield a, a+b, c
    yield b, a+b, c


def _Factors(x):
  i = 1
  j = x
  while i <= j:
    if i*j == x:
      yield i, j
    i += 1
    j = x / i
    

