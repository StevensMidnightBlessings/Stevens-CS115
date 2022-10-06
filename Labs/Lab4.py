"""

I pledge my honor that I have abided by the Stevens Honor System.
CS115 Lab 4
"""

#if nothing in museum return $ as 0
#if knapsack = 0, return []

def knapsack(capacity, itemList):
    """takes int(capacity) and list(itemList), returns max value of List without
       exceeding the capcacity"""
    if itemList == [] or capacity == 0:
        return [0,[]]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        useit = [knapsack(capacity - itemList[0][0], itemList[1:])[0] + itemList[0][1],
                [itemList[0]] + knapsack(capacity - itemList[0][0], itemList[1:])[1]]
        loseit = knapsack(capacity, itemList[1:])
        if useit[0] > loseit[0]:
            return useit
        else:
            return loseit

    
