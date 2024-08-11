#!/usr/bin/python3
"""
File:
0x02-minimum_operations/0-minoperations.py
This project was adopted from a fellow student
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    """
    # end_str = "H"
    # copy_str = ""

    # str_len = 1
    # oper_total = 0

    # while str_len < n:
    #     if n % str_len == 0:
    #         copy_str = end_str  # copy
    #         oper_total += 1
    #     end_str += copy_str     # paste
    #     str_len = len(end_str)
    #     oper_total += 1
    # return oper_total
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
