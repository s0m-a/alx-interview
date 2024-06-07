#!/usr/bin/python3
""" Making changes """


def make_change(coins, total):
    """
    Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0

    check = [float('inf')] * (total + 1)
    check[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            check[amount] = min(check[amount], check[amount - coin] + 1)

    return check[total] if check[total] != float('inf') else -1
