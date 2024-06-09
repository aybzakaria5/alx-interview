#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Finds the minimum number of coins needed to achieve a given total.

    Args:
        coin_values (list): The values of the coins available.
        target_amount (int): The target amount to reach.

    Returns:
        int: The minimum number of coins needed to reach the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coin values in descending order to start
    # with the largest denominations
    sorted_coin_values = sorted(coin, reverse=True)
    remaining_amount = total
    total_coins = 0

    for coin in sorted_coin_values:
        while remaining_amount >= coin:
            remaining_amount -= coin
            total_coins += 1
        if remaining_amount == 0:
            break

    # If loop exits and there is remaining amount
    # we cannot meet the target amount
    if remaining_amount > 0:
        return -1

    return total_coins
