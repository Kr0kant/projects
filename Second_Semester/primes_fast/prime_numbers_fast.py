from math import sqrt
from numba import njit


@njit
def is_prime(num):
    n = 0
    for i in range(1, int(sqrt(abs(num))) + 1 ):
        if abs(num) % i == 0:
            n += 1
    return n == 1 and num > 1 

@njit
def primes_fast(n):
    P = []
    for i in range(n + 1):
        if is_prime(i) == True:
            P.append(i)
    return(P)

