#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """makeChange func"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if coin <= total:
            num_coins += total // coin
            total %= coin

    if total != 0:
        return -1

    return num_coins
