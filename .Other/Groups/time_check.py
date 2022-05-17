from even_permutations import An_group
from fast_even_permutations import An_group_fast
import time


tau = time.time()
An_group(15)
print(time.time() - tau)

tau = time.time()
An_group_fast(15)
print(time.time() - tau)
