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

arg = sys.argv[1]

try:
    arg = int(arg)
except ValueError:
    print('N must be a number')
    sys.exit(1)

if arg < 4:
    print('N must be at least 4')
    sys.exit(1)

n = arg
all_placement = []
possible_placement = []
# populate list with all chesss positions
for row in range(n):
    for col in range(n):
        possible_placement.append([row, col])


def nqueens(n):
    """nqueens solution using backtracking and recursion"""
    global possible_placement
    global all_placement

    if n == 1:
        return

    n -= 1

    for placement in possible_placement:
        # print(placement)
        if not valid_placement(placement, all_placement):
            #print(n)
            continue
        all_placement.append(placement)
        print(all_placement)
        nqueens(n)
        if all_placement:
            print(all_placement)


def valid_placement(placement, all_placement):
    """Checks if the placement of a queen is valid"""
    for queen in all_placement:
        if placement[1] == queen[1]:  # same column
            return False
        elif placement[0] == queen[0]:  # same row
            return False
        # diagonals
        elif placement[0] - placement[1] == queen[0] - queen[1]:
            return False
        elif sum(placement) == sum(queen):
            return False

    return True


if __name__ == '__main__':
    nqueens(n)
