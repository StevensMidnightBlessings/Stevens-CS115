############################################################
# Name:
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    """Returns n as its reciprocal(decimal)"""
    return 1 / x


def add(x, y) :
    """adds x and y"""
    return x + y


def e(n):
    """Returns the approximate value of e by using a Taylor expansion method."""
    list1 = list(map(factorial, list(range(n+1))))
    return reduce(add, map(inverse,list1))


