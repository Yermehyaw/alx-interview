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

    for byte in data:
        byte_to_char = 0

        if byte_to_char > 0:
            # Check for continuation bytes to complete a char
            if byte >> 6 != 0b10:
                return False
            byte_to_char -= 1

        else:
            # Check for lead byte
            if byte >> 7 == 0:
                byte_to_char = 0
            elif byte >> 5 == 0b110:  # single-byte char
                byte_to_char
