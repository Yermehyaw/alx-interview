#!/usr/bin/python3
"""
Making change dynamic programming solution

Modules imported:
maths.min

"""


def makeChange(coins, total):
    """Returns the least no of change for total using denominations in coins
    """
    if not coins or total <= 0:
        return 0

    # Iterative
    count = 0
    for coin in coins:
        if coin <= total:
            temp = total - coin
            count += 1

        if temp == 0:
            return count

    return -1

    # recursive
    if total <= 0:
        return total

    for i in range(len(coins)):
        total = total - coins[i]
        makeChange(coins, total)
        if total == 0:
            return i

    return -1
