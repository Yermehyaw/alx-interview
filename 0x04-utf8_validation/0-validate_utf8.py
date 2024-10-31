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

    encoding = [
        ['01000'],
        ['11000', '10000'],
        ['11100', '10000', '10000'],
        ['11110', '10000', '10000', '10000']
    ]

    try:
        # convert to binary,remove the appended '0b' and fill up to 8 digits
        bin_chars = [bin(char)[2:].zfill(8) for char in data]
    except TypeError:  # if elem is not an int
        return False

    # extract the first 5 bits from each 8 bits digits
    start_bit = [bin_val[:-3] for bin_val in bin_chars]
    print(start_bit)
    print(bin_chars)

    no_bits = len(start_bit)

    i = 0
    while i < no_bits:
        prefix = start_bit[i]
        if prefix == '11110':
            if [
                    start_bit[i],
                    start_bit[i + 1],
                    start_bit[i + 2],
                    start_bit[i + 3]
            ] == encoding[3]:
                continue
            else:
                return False
        elif prefix[:-1] == '1110':
            print(f'prefix is: {prefix[:-1]}')
            pass
        elif prefix[:-2] == '110':
            pass
        elif prefix[:-3] == '01':
            pass
        else:  # prefix/lead byte cannot start with anything else e.g '10'
            return False
        i += 1
    return True

if __name__ == '__main__':
    validUTF8([229, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33])
