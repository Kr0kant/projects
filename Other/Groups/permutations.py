import itertools

def Sn_group(n):
    
    X = []
    for i in range(n):
        X.append(i+1)

    perm_set = itertools.permutations(X)

    return perm_set


