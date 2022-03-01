from numpy.random import uniform
from numpy import array, concatenate

def vgauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)  # concatenate заодно и скопирует
    d = len(ab) # размер по старшему измерению

    # прямой
    for i in range(d):
        ab[i] = ab[i] / ab[i,i]

        for j in range (i+1, d):
            ab[j] = ab[j] - ab[i]*ab[j,i]

    # обратный
    for i in range(d - 1, -1, -1):
        for j in range (i+1, d):
            ab[i] -= ab[j]*ab[i,j]


    x = ab[:, -1]  # Последний столбец
    return (x)