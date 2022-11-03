'''
DISCLAIMER!!!!

These are my solutions I solved with endless sweat. I'm posting these to show companies my work.
'''

fibbonacci = """

# Input: n
# Assume: n > 0
# Output: n

0       read    r1         # Get n
1       setn    r2 0       # sets r2
2       setn    r3 1       # sets r3
3       jeqzn   r1 10      # if n = 0, jump to line 9 and ends
4       add     r4 r2 r3   # else: makes r4 = r2 + r3
5       write   r2         # returns r2
6       addn    r1 -1      # does (n-1) --> r1 = r1 - 1
7       copy    r2 r3      # makes r2 = r3
8       copy    r3 r4      # makes r3 = r4
9       jumpn   3          # goes back to jeqzn
10      halt               # stops!

"""
