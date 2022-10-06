############################################################
# Name:
# Pledge:I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#  
############################################################

def same(word):
    if word[0].casefold() == word[-1].casefold():
        return True
    else:
        return False

def consecutiveSum(x, y):
    sum = ((x+y) / 2) * (y - x - 1)
    return sum
