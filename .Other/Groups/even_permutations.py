from permutations import Sn_group


def An_group(n):

    perm_set = Sn_group(n)

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

print(An_group(2))
