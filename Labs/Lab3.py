"""

I pledge my honor that I have abided by the Stevens Honor System.
CS115 Lab 2
"""

def change(amount, coins):
    """amount: non negative int, indicating amount of money to be made.
       coins: list of coin values with 1 always in the list.
       returns non negative int of minimum number of coins needed to equal amount"""

    if amount <= 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        useit = 1 + change(amount - coins[0], coins)
        loseit = change(amount, coins[1:])
        return min(useit, loseit)



