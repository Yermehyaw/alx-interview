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

