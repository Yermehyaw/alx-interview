#!/usr/bin/python3
"""
Making change dynamic programming solution

Modules imported:
maths.min

"""


def makeChange(coins, total):
    """Making change using arbitrary coin denominations
    """
    if not coins or total <= 0:
        return 0
