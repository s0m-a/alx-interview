#!/usr/bin/python3
"""Making changes"""


def make_change(coins, target):
    """
    Generate changes needed to reach total
    
    Args:
        coins (List[int]): List of coin denominations
        target (int): Target amount to reach
    
    Returns:
        int: Fewest number of coins needed to meet the target amount,
             or -1 if it's not possible to make the target amount with the available coins
    """
    table = [float('inf')] * (target + 1)
    table[0] = 0  # Base case: 0 coins needed to make an amount of 0
    
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                table[amount] = min(table[amount], table[amount - coin] + 1)
    
    if table[target] == float('inf'):
        return -1
    else:
        return table[target]

