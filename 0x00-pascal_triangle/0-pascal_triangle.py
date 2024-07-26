#!/usr/bin/python3
"""
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    This function will generate Pascal's Triangle
    and return it as a list of lists of integers. 
    We'll ensure it handles the case when n <= 0 
    by returning an empty list.
    """
    arr = []
    if n <= 0:
        return []
    for i in range(n):
        temp_arr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_arr.append(1)
            else:
                temp_arr.append(arr[i - 1][j - 1] + arr[i - 1][j])
        arr.append(temp_arr)
    return arr
