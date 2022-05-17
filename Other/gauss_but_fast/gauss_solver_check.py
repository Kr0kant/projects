from gauss_solver import vgauss, test_error
from gauss_solver_fast import vgauss_fast
from numpy import array
import time


#tau = time.time()
#test_error(vgauss)
#print(time.time() - tau)

tau = time.time()
test_error(vgauss_fast)
print(time.time() - tau)
