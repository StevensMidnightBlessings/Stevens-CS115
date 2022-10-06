'''
Created on 9/26/22
@author:   
Pledge:  I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
import functools
from functools import reduce
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.



def letterScore(letter, scorelist):
    """takes a char and a list (each element is a char), returns the number associated with the char."""
    g = scorelist[0][0]
    if letter == g:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    """takes a string and scorelist (lowercase) and returns scramble score of string"""
    #basecase
    if S == "":
        return 0
    else:
        return wordScore(S[1:], scorelist) + letterScore(S[0], scorelist)

def check2(letter, Rack):
    """Takes a letter and removes from Rack"""
    if Rack == []:
        return []
    elif letter == Rack[0]:
        return Rack[1:]
    else:
        return [Rack[0]] + check2(letter, Rack[1:])

def check(word, Rack):
    """checks if theres a word that can be made"""
    if word == "":
        return True
    elif word[0] in Rack:
        return check(word[1:], check2(word[0], Rack))
    else:
        return False
    
def scoreList(Rack):
    """takes an input Rack(lowercase) and returns a list of all the words in the global dictionary that can
        be made from those letters and the score for each one"""
    return list(map(lambda word: [word, wordScore(word, scrabbleScores)], filter(lambda word: check(word, Rack), Dictionary)))

def bestWord(Rack):
    """takes an input Rack, returns a list with 2 elements: the highest scoring word and its score."""
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ["", 0]
    else:
        return functools.reduce(lambda i, j: i if i[1] > j[1] else j, scorelist)
