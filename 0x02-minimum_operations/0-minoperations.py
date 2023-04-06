#!/usr/bin/python3

"""
    method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
        initialization
    """

    current = 1
    init = 0
    temp = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            init = current
            current += init
            temp += 2
        else:
            current += init
            temp += 1
    return temp
