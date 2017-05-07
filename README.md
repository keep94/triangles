# triangles

Python code to generate non right triangles with all integer sides and one
integer angle.

# Introduction

There exist and infinite number of right triangles with integer sides as
a^2 + b^2 = c^2 has an infinite number of integer solutions. Using the law
of cosines, one can generate an infinite number of triangles with integer
sides and a 120 degree angle because a^2 + b^2 + ab = c^2 has an infinite
number of integer solutions as well. Similarly, one can generate an infinite
nuber of triangles with integer sides and a 60 degree angle because 
a^2 + b^2 - ab = c^2 also has an infinite number of integer solutions.

# The python code

## triangles.Triangles120()

triangles.Triangles120 generates triangles with integer sides and a 120 degree
angle. The code below returns 10 such triangles.

```
>>> import itertools
>>> import triangles
>>> list(itertools.islice(triangles.Triangles120(), 10))
[(3, 5, 7), (5, 16, 19), (6, 10, 14), (7, 8, 13), (7, 33, 37), (9, 15, 21), (9, 56, 61), (10, 32, 38), (11, 24, 31), (12, 20, 28)]
```

## triangles.Triangles60()

triangles.Triangles60 generates triangles with integer sides and a 60 degree
angle. The code below returns 10 such triangles.

```
>>> import itertools
>>> import triangles
>>> list(itertools.islice(triangles.Triangles60(), 10))
[(3, 8, 7), (5, 8, 7), (5, 21, 19), (16, 21, 19), (6, 16, 14), (10, 16, 14), (7, 15, 13), (8, 15, 13), (7, 40, 37), (33, 40, 37)]
```

