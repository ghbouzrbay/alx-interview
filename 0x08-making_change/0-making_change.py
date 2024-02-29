#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    min_coins = total + 1
    for coin in coins:
        if coin <= total:
            num_coins = 1 + makeChange(coins, total - coin)
            if num_coins < min_coins:
                min_coins = num_coins
    if min_coins > total:
        return -1
    return min_coins
