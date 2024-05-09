#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """
    Write a method that determines
    if a given data set represents a valid UTF-8 encoding.
    """
    x = len(data)
    jump = 0
    for i in range(x):
        if jump > 0:
            jump -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            jump = 0
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if x - i >= span:
                next = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next):
                    return False
                jump = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if x - i >= span:
                next = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next):
                    return False
                jump = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if x - i >= span:
                next = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next):
                    return False
                jump = span - 1
            else:
                return False
        else:
            return False
    return True
