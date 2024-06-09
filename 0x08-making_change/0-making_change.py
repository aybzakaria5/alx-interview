#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to achieve the target amount.
    """
    if total < 1:
        return 0

    coins.sort(reverse=True)
    coin_count = 0

    for value in coins:
        if total == 0:
            break
        max_coins = total // value
        total -= max_coins * value
        coin_count += max_coins
    if total != 0:
        return -1
    return coin_count
