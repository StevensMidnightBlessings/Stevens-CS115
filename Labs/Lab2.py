"""

I pledge my honor that I have abided by the Stevens Honor System.
CS115 Lab 2
"""



def dot(L, K):
    """takes in L and K, lists of numbers. If L and K are equal it will iterate
       and return the sum of the first elements of both list and so on. If lists
       are empty then it will return 0.0"""
    if L == []:
        return 0.0
    else:
        return (L[0] * K[0]) + dot(L[1:], K[1:])    


def explode(S):
    """takes a string input and returns every letter in the string"""
    
    if (S) == "":
        return []
    else:
        return [S[0]] + explode(S[1:])


def ind(e, L):
    """takes element e and sequence L, returns the index in which e is first found in
    L"""
    if len(L) == 0   :
        return 0
    if e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])
        


def removeAll(e, L):
    """takes an element(e) and a list(L) and returns a new list with all the elements
    identical to e"""
    if L == []:
        return []
    elif L[0] != e:
        return [L[0]] + removeAll(e, L[1:])
    else:
        return [] + removeAll(e, L[1:])


def myFilter(f, L):
    """akljfd"""

    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return [] + myFilter(f, L[1:])


def deepReverse(L):
    """takes a list of elements (some elements may be lists) returns the list but reversed"""
    if L == [] :
        return []
    elif isinstance(L[-1], list) :
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1  ])
  
  
