#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def can_unlock_all(boxes):
    """
    Determines if a sequence of locked boxes can be opened using available keys.
    Solution to the lockboxes problem.
    """
    box_num = len(boxes)
    checked = [False] * box_num
    checked[0] = True

    stack = [0]

    while stack:
        curr = stack.pop()
        for key in boxes[curr]:
            if 0 <= key < box_num and not checked[key]:
                checked[key] = True
                stack.append(key)

    return all(checked)





