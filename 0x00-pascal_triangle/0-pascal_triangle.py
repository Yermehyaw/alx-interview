#!/usr/bin/python3
"""
Modules Imported: None

"""


def pascal_triangle(n):
    """
    Returns a lost if losts representing a pascal triangle with n
    number of rows

    Args:
    n(int): no of rows in pascals triangle

    Return:
    list of lists

    """
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = []
    primary_list = [1]
    triangle.append(primary_list)

    if n == 1:
        return triangle

    base_list = [1, 1]  # list which will be summed to get elem of sucsve rows
    triangle.append(base_list)

    if n == 2:
        return triangle

    elif n > 2:
        rem_rows = n - 2  # remaining lists to be appended to triangle
        for i in range(rem_rows):
            temp_list = []
            temp_list.append(1)  # constant starting value in pascal triangle

            # Placing values in temp_list indexes
            idx = 1
            bl_idx = 0  # base list index
            while idx < n:
                temp_list.append(base_list[bl_idx] + base_list[bl_idx + 1])
                idx += 1
                bl_idx += 1
                if idx == len(base_list):  # no number pair left in base_list
                    temp_list.append(1)  # constant ending value
                    break  # new list/row has is completed

            triangle.append(temp_list)
            base_list = temp_list  # prep for next posdible iteration

    return triangle
