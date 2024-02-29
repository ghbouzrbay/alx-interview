#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    if total in memo:
        return memo[total]
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(sorted_coins)
    while rem > 0:
        if coin_idx >= n:
            memo[total] = -1
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            num_coins = rem // sorted_coins[coin_idx]
            rem %= sorted_coins[coin_idx]
            coins_count += num_coins
        else:
            coin_idx += 1
    memo[total] = coins_count
    return coins_count

memo = {}
