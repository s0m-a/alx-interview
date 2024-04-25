#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    
    Args:
        n (int): The desired number of H characters.
    
    Returns:
        int: The fewest number of operations needed to reach n H characters. If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return n

    # Initialize variables
    operations = 0
    clipboard = 1
    buffer = 1

    while buffer < n:
        if n % buffer == 0:
            clipboard = buffer
            operations += 1
        buffer += clipboard
        operations += 1

    return operations

