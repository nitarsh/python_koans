#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    throw_exception_if_invalid_triangle(a, b, c)
    if a == b == c: return 'equilateral'
    if a != b != c and a != c != b: return 'scalene'
    return 'isosceles'


def throw_exception_if_invalid_triangle(a, b, c):
    if a < 1 or b < 1 or c < 1: raise TriangleError, "My Message"
    s = sorted((a, b, c))
    if s[2] > s[0] + s[1]: raise TriangleError, "My Message"


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
