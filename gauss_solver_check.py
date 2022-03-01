from gauss_solver import vgauss
from matrix_generator import test_error
from numpy import array

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)


solution = vgauss(a, b)
print(solution)


print(test_error(vgauss))

