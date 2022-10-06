"""

I pledge my honor that I have abided by the Stevens Honor System.
CS115 Lab 2
"""

import math
import functools

def mult(x,y):
    """returns the product of x and y"""
    return x * y


def factorial(n):
    """takes a positive integer n and returns the factorial"""

    return functools.reduce(mult, range(1,n + 1)) 



def add(x, y):
    """adds x and y and returns the sum"""
    return x + y

def mean(L):
    """takes a list as an ainput and returns the average value in the list"""
    newList = functools.reduce(add, L)
    return ((newList / len(L)))
