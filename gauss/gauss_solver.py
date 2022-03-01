from numpy.linalg import norm, det
from numpy.linalg import solve as solve_out_of_the_box
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


N=40
SMALL = 1e-5

def test_error(solver_function):
    # Сгенерируем хорошо обусловленную систему
    while True:
        a = uniform(0.0, 1.0, (N, N))
        b = uniform(0.0, 1.0, (N,  ))

        d = det(a)
        if abs(d) <= SMALL:  # Определитель маленький — плохо
            # print(f"det: {d}")
            continue  # Попробуем ещё
        if d < 0.0:  # Отрицательный — поменяем знак
            # print(f"det: {d}")
            a = -a

        try:
            oob_solution = solve_out_of_the_box(a, b)
        except Exception as e:  # Всё-таки система плохая
            # print(f"exc: {e}")
            continue  # Попробуем ещё

        sb = a @ oob_solution
        if norm(sb - b, ord=1) > SMALL:
            # print("Bad solution...")
            continue  # Всё же не очень система получилась =)
        
        break # Всё, считаем, что мы случайно сгенерировали хорошую систему

    tested_solution = solver_function(a, b)
    return norm(tested_solution - oob_solution, ord=1)