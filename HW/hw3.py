'''
Created on 10/7/22
@author:   
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

#order doesn't matter
#first element = # of coins used

def giveChange(numberOfCoins, listOfCoins):
    '''takes amount and a list of coins, returns the a list of coins equaling
    the amount''' 
    #base case
    if numberOfCoins == 0:
        return [0, []]
    elif listOfCoins == []:
        return [float("inf"), []]
    elif listOfCoins[0] > numberOfCoins:
        return giveChange(numberOfCoins, listOfCoins[1:])
    else:
        useHelp = giveChange(numberOfCoins - listOfCoins[0], listOfCoins)
        useit = [(1 + useHelp[0]), ([listOfCoins[0]] + useHelp[1])]
        loseHelp = giveChange(numberOfCoins, listOfCoins[1:])
        loseit = [loseHelp[0], loseHelp[1]]
        if useit[0] < loseit[0]:
            return useit
        else:
            return loseit


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
def letterScore(letter, lst):
    '''takes a single letter and a list, returns the value of that letter'''
    if lst == []:
        return 0
    elif lst[0][0] == letter:
        return lst[0][1]
    else:
        return letterScore(letter, lst[1:])

def wordScore(S, scorelist):
    '''takes the string and the scorelist, returns the scrabble score'''
    if len(S) == 0:
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''    
    if dct == []:
        return []
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''

    if n == 0:
        return []
    elif L == []:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''

    if n == 0:
        return L
    elif L == []:
        return L
    else:
        return drop(n-1, L[1:])

