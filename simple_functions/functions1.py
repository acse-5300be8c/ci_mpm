from functools import cache
import numpy as np


__all__ = ['my_sum', 'factorial', 'sinee']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n*factorial(n-1) if n else 1


def sinee(n, nterms=15):
    num_pattern = [0, 1, 0, -1]
    num = np.resize(num_pattern, (nterms, ))

    vector_factorial = np.vectorize(factorial)
    denom = np.arange(nterms)
    denom = vector_factorial(denom)
    denom[denom == 0] = 1

    mult = n ** np.arange(nterms)
    answer = (num/denom * mult)

    return answer.sum()
