#!/usr/bin/python3

"""0. Minimum Operations"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    
    Args:
        n (int): The desired number of H characters.
    
    Returns:
        int: The fewest number of operations needed to reach n H characters. If n is impossible to achieve, returns 0.
    """

    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
