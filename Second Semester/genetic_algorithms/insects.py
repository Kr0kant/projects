from graphics import tree
import turtle as tl
from life import reproduction
from life import growing

mother = [[2, 20, 4, 12], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0]]

#[2, 20, 4, 6]

for i in range(100):
    tl.clearscreen()
    tl.left(90)
    tl.speed(0)
    tl.hideturtle()
    tl.tracer(0, 0)
    
    reproduction(mother)
    growing(mother)
    for j in range(1, 9):
        tl.penup()
        tl.goto(-400+100*j, 0)
        tl.pendown()

        tree(mother[j][0], mother[j][1], mother[j][2]/10, mother[j][3]*10)



    winner = int(input())
    mother = [mother[winner], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0], 4*[0]]