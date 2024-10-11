#!/usr/bin/python3
"""
Implement an algorithm to solve if a variable no of lockboes can be opened

Modules Imported: None

"""


def canUnlockAll(boxes):
    """
    Return true or false if the all the boxes can be opened

    Args:
    boxes(list); List of lists of ints(repr keys)

    Return:
    bool

    """
    no_boxes = len(boxes)
    available_keys = set()

    for box in boxes:
        # get the keys from each box and save to a set
        keys = box
        available_keys.update(keys)

    # sort the unique keys in the set
    sorted_keys = sorted(available_keys)  # now a list
    # print(sorted_keys)

    # create an ideal list of what the keys should be
    all_keys = [(no_boxes - 1) for i in range(no_boxes)]  #
    all_keys.sort()
    # print(all_keys)

    if len(sorted_keys) == (no_boxes - 1):
        """
        # we know we have same no unique keys as with the no of boxes
        # but are these unique keys capable of opeming each box i.e do they
        match each individual box?, asides the already opened 0th box)

        i = 0
        for key in sorted_keys:
            if key == 0 and (key not in sorted_keys):
                    continue  # dont check for key 0, box 0 is already open
            print(key)

            if key != all_keys[i]:
                return False
            i += 1
        """
        return True

    return False
