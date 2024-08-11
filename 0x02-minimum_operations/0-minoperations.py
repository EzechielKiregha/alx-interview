#!/usr/bin/python3
"""
In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste.

"""


def minOperations(n : int) -> int:
    """if n = 9
    then the Number of operations will be 6
    H => Copy All => Paste => HH => Paste =>HHH =>
    Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

    Args:
        n (int): Given a number n, write a method that
        calculates the fewest number of operations
        needed to result in exactly n H characters in the file.

    Returns:
        int: If n is impossible to achieve, return 0
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
