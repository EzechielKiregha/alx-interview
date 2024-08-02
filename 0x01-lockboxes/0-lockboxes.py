#!/usr/bin/python3
"""this is an interview question on lockboxes"""


def canUnlockAll(boxes):
    """Ensure the use of a set for visited boxes
    for O(1) average-time complexity for checks.
    Use iterative DFS or BFS to avoid stack overflow issues
    with recursion.
    Optimize by skipping already visited boxes early in the traversal.

    Args:
        boxes (List[List[int]]): boxes is a list of lists

    Returns:
        bool: True if all boxes can be opened, else return False
    """
    from copy import deepcopy

    # checks if given valid list of boxes
    if type(boxes) is not list or len(boxes) < 1:
        return False
    for box in boxes:
        if type(box) is not list:
            return False
    # creates a copy of boxes to not affect the original list of lists
    copy_boxes = deepcopy(boxes)
    # creates list of available keys (only contains 0 initially)
    keys_list = [0]
    # while there are still available keys:
    while len(keys_list) > 0:
        # the current key will be the first available key
        key = keys_list[0]
        # keys list will reset to remove used key
        keys_list = keys_list[1:]
        if type(key) is int and key >= 0:
            copy_boxes[key].append(-1)
            for new_key in copy_boxes[key]:
                if new_key == -1:
                    # if new key is -1 flag to marks as opened, continue
                    continue
                if new_key >= len(copy_boxes):
                    # if new key is out of range for the boxes, continue
                    continue
                if -1 in copy_boxes[new_key] or new_key in keys_list:
                    # if box key is known, continue
                    continue
                # update the list of available key
                assert isinstance(new_key, object)
                keys_list.append(new_key)
            continue
        # checks if given valid key
        return False
    for box in copy_boxes:
        if -1 not in box:
            # if a box is missing the -1 flag, it was not unlocked
            return False
    # returns true if all boxes in the previous loop were indicated as unlocked
    return True
