from numba import njit
from permutations import Sn_group

@njit
def An_group_fast(n, perm_set):

    
    An = []

    for h in perm_set:
        inv = 0
        for i in range (n):
            for j in range (i+1, n):
                if h[i] > h[j]:
                    inv += 1
        if (inv % 2) == 0:
            An.append(h)
    
    return An



print(An_group_fast(5, Sn))
