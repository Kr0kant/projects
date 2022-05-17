from math import sqrt

def is_prime(num):
    n = 0
    for i in range(1, int(sqrt(abs(num))) + 1 ):
        if abs(num) % i == 0:
            n += 1
    return n == 1 and num > 1 


def primes(n):
    P = []
    for i in range(n + 1):
        if is_prime(i) == True:
            P.append(i)
    return(P)

