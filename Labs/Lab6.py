'''
Created on 10/20/22
@author:  
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 1:
        return True
    else:
        return False
# 101010
# 32 + 0 + 8 + 0 + 2 + 0 = 42


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    elif n == 2:
        return "10"
    elif isOdd(n) == True:
        return numToBinary(n // 2) + "1"
    else:
        return numToBinary(n // 2) + "0"


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif s == "0":
        return 0
    elif s == "1":
        return 1
    elif s[0] == "1" and s!="1":
        return 2**(len(s)-1) + binaryToNum(s[1:]) 
    else:
        return binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == "00000000":
        return "00000001"
    elif s == "11111111":
        return "00000000"
    elif s[0] == "0":
        return increment(s[1:])
    else:
        return '0' * (8 - len(numToBinary(binaryToNum(s) + 1)))+ numToBinary(binaryToNum(s)+ 1)

    

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else:
        print(s)
        return count(increment(s), n - 1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    elif n == 2:
        return "2"
    elif n == 3:
        return "10"
    elif n % 3 == 0:
        return numToTernary(n // 3) + "0"
    elif n % 3 == 1:
        return numToTernary(n // 3) + "1"
    else:
        return numToTernary(n // 3) + "2"

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    elif s == "1":
        return 1
    elif s == "2":
        return 2
    elif s[0] == "2" and s != "2":
        return 2 * 3 ** (len(s) - 1) + ternaryToNum(s[1:])
    elif s[0] == "1" and s != "1":
        return 3 ** (len(s)- 1) + ternaryToNum(s[1:])
    else:
        return ternaryToNum(s[1:])


'''
Questions

For an odd base 2 and 10, the right most bit, 2^0 will be 1. 
For even, 2^0 will be 0.
2^0 is the only odd number which is 1.


It will just do integer division by the base, 2 in this case.


even: use recursion and add 0 at the end
odd: use recursion and add 1 at the end


Ternary of 59: 2012
 - divide 59 by 3 and write remainders
 59 / 3 = 19r2
 19 / 3 = 6r1
 6 / 3 = 2r0
 2 / 3 = r2
 the remainders = 2012
'''
