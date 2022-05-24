from random import randint, choice



def reproduction(mother):
    for i in range(1,9):
        a = randint(0, 3)
        b = choice((-1, 1))
        mother[i][a] = mother[0][a] + b
        if mother[i][a]<0:
            mother[i][a] = 0
        if mother[i][0] > 7:
            mother[i][0] = 7


def growing(mother):
    for i in range(1, 9):
        for j in range(0, 4):
            b = randint(-1, 2)
            mother[i][j] = mother[0][j] + b
            if mother[i][j]<0:
                mother[i][j] = 0
            if mother[i][0] > 7:
                mother[i][0] = 7
