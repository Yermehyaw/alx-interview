#!/usr/bin/python3
"""
The perimeter of land(1s) in water(0s) arranged as a list of lists


pseudocode:
GET all indexes with a 1
IF indexes have the same row
  SUM the indexes as width
IF indexes has the same col
"""


def island_perimeter(grid):
    """Returns the perineter of 1s in a list of lists"""
    if not grid or not isinstance(grid, list):
        return 0

    earth = []
    for x in range(len(grid)):  # no of rows is x
        for y in range(len(grid[x])):  # no of cols is y
            if grid[x][y] == 1:
                earth.append([x, y])

#    return earth
    # evaluate coordinates where there is earth to derive perim of land
    earth_no = len(earth)
    perimeter = 4 * earth_no  # ideal permieter if each were separate
    # find matching coordinates and deduct from ideal perimeter
    for i in range(earth_no):
        j = 1  # greater than i by 1 step
        if earth[i][0] == earth[i][1]:  # each row has an index of 0 & 1
            perimeter -= 1
        if earth[i][1] == earth[i][0]:
            perimeter -= 1

        """"
        if earth[j][0] == earth[j][1]:
            perimeter -= 1
        if earth[j][1] == earth[j][0]:
            perimeter -= 1
        """

        if earth[i][0] == earth[j][0]:
            perimeter -= 1
        if earth[i][1] == earth[j][1]:
            perimeter -= 1
        if earth[j][1] == earth[i][1]:
            perimeter -= 1
        if earth[j][0] == earth[i][0]:
            perimeter -= 1
        j += 0

    return perimeter
