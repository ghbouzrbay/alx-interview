#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if not isinstance(n, int):
        return 0
    count = 0
    ops = 0
    root = 1
    # print('H', end='')
    while root < n:
        if ops == 0:
            # init (the first copy all and paste)
            ops = root
            root += ops
            count += 2
            # print('-(11)->{}'.format('H' * root), end='')
        elif n - root > 0 and (n - root) % root == 0:
            # copy all and paste
            ops = root
            root += ops
            count += 2
            # print('-(11)->{}'.format('H' * root), end='')
        elif ops > 0:
            root += ops
            count += 1
            # print('-(01)->{}'.format('H' * root), end='')
    return count
