#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias = 0
    bens = 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        count = len(list(filter(lambda x: x, primes[0: n])))
        bens += count % 2 == 0
        marias += count % 2 == 1
    if marias == bens:
        return None
    return 'Maria' if marias > bens else 'Ben'

