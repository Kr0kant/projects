from gcd_euklid import gcd
from gcd_fast import gcd_fast
import time

gcd_fast(10, 2)

tau = time.time()
print(gcd(8374147767264764208736437648, 83764872625245425352424240204))
print(time.time() - tau)

tau = time.time()
print(gcd_fast(8374147767264764208736437648, 83764872625245425352424240204))
print(time.time() - tau)
