from prime_numbers import primes
from prime_numbers_fast import primes_fast
import time

primes_fast(10)

tau = time.time()
primes(1000000)
print(time.time() - tau)

tau = time.time()
primes_fast(1000000)
print(time.time() - tau)
