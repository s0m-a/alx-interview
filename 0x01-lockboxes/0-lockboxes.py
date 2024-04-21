#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines if a sequence of locked boxes can be opened using available keys.
    Solution to the lockboxes problem.
    """
    boxNum = len(boxes)
    checked = [False] * boxNum
    checked[0] = True

    stack = [0]

    while stack:
        curr = stack.pop()
        for key in boxes[curr]:
            if 0 <= key < boxNum and not checked[key]:
                checked[key] = True
                stack.append(key)

    return all(checked)
