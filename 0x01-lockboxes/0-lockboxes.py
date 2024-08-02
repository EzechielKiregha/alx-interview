#!/usr/bin/env python3
"""
In this module,
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


from typing import List


def canUnlockAll(boxes : List[List[int]]) -> bool:
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
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key < len(boxes) and key not in visited:
                    stack.append(key)
    
    return len(visited) == len(boxes)
