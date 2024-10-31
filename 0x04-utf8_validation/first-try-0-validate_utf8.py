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

    lead_bytes = [
        '1111',
        '1110',
        '1100',
        '0111',
        '0110',
        '0101',
        '0100',
        '0011',
        '0010',
        '0001',
        '0000'
    ]

    try:
        # convert to binary,remove the appended '0b' and fill up to 8 digits
        bin_chars = [bin(char)[2:].zfill(8) for char in data]
        # bin_chars = [int(bin(char)) for char in data]
    except TypeError:  # if elem is not an int
        return False

    # extract the first 4 bits(nibble) from each 8 bits digits
    start_nibble = [bin_val[:-4] for bin_val in bin_chars]

    # mask = [0b11111000, 0b11110000, 0b11100000, 0b11000000, 0b100000000]

    print(bin_chars)
    print(start_nibble)

    prefix = start_nibble[0]

    if prefix not in lead_bytes:  # first byte in data isnt a lead byte
        return False  # invalid/corrupt utf-8 chars

    total = len(start_nibble)  # no of nibbles/bytes
    counter = 0  # counts no of iterations
    char_count = 0  # coints no of characters validated
    for byte in bin_chars:
        if byte[:4] in lead_bytes and counter == 0:
            counter += 1
            char_count += 1
        elif char_count == 0:  # no lead byte
            return False
        elif byte[:2] == '10':
            counter += 1
        elif char_count > 0 and counter < total:  # invalid utf encoding
            return False
        else:  # new lead_byte reached
            counter = 0
    return True #   # last byte reached successfully

    if prefix == '11110':
        pass
    elif prefix[:-1] == '1110':
        print(f'prefix is: {prefix}')
        pass
    elif prefix[:-2] == '110':
        pass
    elif prefix[:-3] == '01':
        pass
    else:  # prefix/lead byte cannot start with anything else e.g '10'
        return False
    #return True

    # first verify the lead byte is valid
    # if 4 byte, check next 3 consecutive bytes, if they begin with 10
    # if 3 byte, check next 2 consecutive bytes, if they begin with 10
    # if 2 bytes, check if next byte begins with 10
    # otherwise check if it begins with 0,
    # if none of ythe above conditions hold, return False as the encoding is corrupt

if __name__ == '__main__':
    validUTF8([229, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33])
