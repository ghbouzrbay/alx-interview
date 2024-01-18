#!/usr/bin/python3
'''the method that calculates the fewest number of
    operations needed to result in exactly n H
    characters in the file
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(i, int):
        return 0
    count = 0
    pi = 0
    ok = 1
    while ok < i:
        if pi == 0:
            pi = ok
            ok += pi
            count += 2
        elif i - ok > 0 and (i - ok) % ok == 0:
            pi = ok
            ok += pi
            count += 2
        elif pi > 0:
            ok += pi
            count += 1
    return count
