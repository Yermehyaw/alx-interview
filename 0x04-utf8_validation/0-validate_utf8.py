#!/usr/bin/python3
"""
Bitwise operations to validate a utf-8 character set

Modules imported: none

"""


def validUTF8(data):
    """
    Returns True if data is a valid utf-8 character/character set

    Args:
    data(list): list of int(s) representing characters
3
    """
    if not isinstance(data, list):
        return False

    count = 0

    for byte in data:
        if not isinstance(byte, int):
            return False

        # Check for continuing bytes that follow a lead byte in making a char
        if count > 0:
            if byte >> 6 != 0b10 and byte >> 5 != 0b010:
                return False  # continuing bytes must start with '10xxxxxx'

            count -= 1

        # Check for lead bytes and adjust their corresponding count accprdingly
        else:
            if byte >> 4 == 0b1111:  # 4 byte char
                count = 3
            elif byte >> 5 == 0b111:  # 3 byte char
                count = 2
            elif byte >> 6 == 0b11:  # 2 byte char
                count = 1
            elif byte >> 7 == 0b0:  # single byte char
                count = 0
            else:  # the above are the only acceptable lead bytes
                return False

    return True
