#!/usr/bin/python3
"""
nqueens problem: finding placement ppsitions for n quuens
on a chessboard without any threatening another

modules imported: sys

"""
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

n = sys.argv[1]

try:
    n = int(n)
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)


def nqueens(n, all_placement=[]):
    """nqueens solution using backtracking and recursion"""
    if len(all_placement) == n:
        print(all_placement)
        return

    for col in range(n):
        row = len(all_placement)
        placement = [row, col]

        if valid_placement(placement, all_placement):
            all_placement.append(placement)
            nqueens(n, all_placement)  # recursion
            all_placement.pop()  # backtracking


def valid_placement(placement, all_placement):
    """Checks if the placement of a queen is valid"""
    for queen in all_placement:
        # same row or col
        if placement[1] == queen[1] or placement[0] == queen[0]:
            return False
        # diagonals
        elif abs(placement[0] - queen[0]) == abs(placement[1] - queen[1]):
            return False

    return True


if __name__ == '__main__':
    nqueens(n)
