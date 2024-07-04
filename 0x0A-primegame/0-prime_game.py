#!/usr/bin/python3
'''Maria and Ben are playing a game "isWinner"'''

PLAYER1_NAME = 'Maria'
PLAYER2_NAME = 'Ben'


def isWinner(x, nums):
    ''' Name of the player that won the most rounds '''
    rounds_1 = 0
    rounds_2 = 0
    memo = {}
    lens = len(nums)

    for i in range(x):
        n = nums[i % lens]

        moves = memo.get(n)
        if moves is None:
            moves = primesCount(n)
            memo[n] = moves

        if moves % 2:
            rounds_1 += 1
        else:
            rounds_2 += 1

    if rounds_1 == rounds_2:
        return None
    elif rounds_1 > rounds_2:
        return PLAYER1_NAME
    else:
        return PLAYER2_NAME


def primesCount(n):
    '''Returns name of the player that won the most rounds of choosing a prime num'''
    isPrime = [True for i in range(n + 1)]
    count = 0

    i = 2
    while i <= n:
        if isPrime[i]:
            if i * i > n:
                break
            count += 1
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
        i += 1

    for i in range(i, n + 1):
        if isPrime[i]:
            count += 1

    return count
