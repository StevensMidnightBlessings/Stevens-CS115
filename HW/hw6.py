POV: you carry your partner and eventually do all the work. 

'''
Created on 10/31/22
@author:   
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
    
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#copied from lab 2
def ind1(S):
    '''takes element s, returns the index in which ones is first found in L'''
    if S == '':
        return 0
    if S[0] == '1':
        return 0
    return ind1(S[1:]) + 1

def ind0(S):
    '''takes element s, returns the index in which zeros is first found in L'''
    if S == '':
        return 0
    if S[0] == '0':
        return 0
    return ind0(S[1:]) + 1

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 1:
        return True
    else:
        return False
    
#copied numToBinary from lab6
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

#copied BinaryToNum from lab6
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

def padding(S):
    '''takes s and returns compressed zeros'''
    return '0' * (COMPRESSED_BLOCK_SIZE - len(S)) + S

def compress(S):
    '''a function that takes a binary string S of length 64 as input and returns
    another binary string as output. Output binary string should be a run-length
    encoding of the input string'''
    ones = ind1(S[:MAX_RUN_LENGTH])
    zeros = ind0(S[ones:ones+MAX_RUN_LENGTH])
    pad1 = padding(numToBinary(ones))
    pad0 = padding(numToBinary(zeros))
    cut1 = S[ones:]
    cut0 = S[zeros:]
    if S == '':
        return ''
    elif cut1 == '':
        return compress(cut1) + pad1
    else:
        return pad1 + pad0 + compress(S[ones+zeros:])


def uncompress(C):
    '''inverts the compressing in the compress function. takes input C and outputs
    S. Sometimes will give output longer than its input. '''
    if C == '':
        return ''
    else:
        #amount of zeros 
        zeros = binaryToNum(C[0:5]) * '0'
        #amount of ones
        ones = binaryToNum(C[5:10]) * '1'
        return zeros + ones + uncompress(C[10:])

def compression(S):
    '''takes input S and returns the ratio of the comopressed size to the original
    size for image S.'''
    return (len(compress(S)) / len(S))
