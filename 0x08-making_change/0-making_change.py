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

    coins.sort(reverse=True)
    current_sum = 0
    coin_index = 0
    coin_count = 0
    num_coins = len(coins)
    while current_sum < total and coin_index < num_coins:
        while coins[coin_index] <= total - current_sum:
            current_sum += coins[coin_index]
            coin_count += 1
            if current_sum == total:
                return coin_count
        coin_index += 1
    return -1
