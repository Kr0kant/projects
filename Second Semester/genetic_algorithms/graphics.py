import turtle as tl
import math


def tree(n, L, gamma, alpha):

    if n == 0:
        return
    
    tl.forward(L)
    tl.left(alpha)
    tree(n-1, gamma*L, gamma, alpha)

    tl.right(2*alpha)
    tree(n-1, gamma*L, gamma, alpha)

    tl.left(alpha)
    tl.forward(-L)
 
 
def ellipse(a, b, color, fill):
    dx = tl.xcor()
    dy = tl.ycor()
    tl.color(color, fill)
    tl.begin_fill()
    for deg in range(361):
        rad = math.radians(deg)
        x = a * math.sin(rad) + dx
        y = -b * math.cos(rad) + b + dy
        tl.goto(x, y)
    tl.end_fill()


def spider(R, a, b, L1, L2, L3, teta):
    tl.penup()
    tl.goto(0, 0)
    tl.pendown()

    tl.circle(int(R))

    tl.penup()
    tl.goto(0, int(R))
    tl.pendown()
 
    ellipse(int(a), int(b), 'black', 'white')   


    
    for i in range (1,3):
        tl.penup()
        tl.goto(0, int(R+b))
        tl.pendown()   

        tl.setheading(90)
        tl.left(30*i)

        tl.penup()
        tl.forward(int(b))
        tl.pendown()

        tl.forward(int(L1))
        tl.right(int(teta))
        tl.forward(int(L2))
        tl.right(int(teta))
        tl.forward(int(L3))

    for i in range (1,3):
        tl.penup()
        tl.goto(0, int(R+b))
        tl.pendown()   

        tl.setheading(0)
        tl.left(30*i)

        tl.penup()
        tl.forward(int(b))
        tl.pendown()

        tl.forward(int(L1))
        tl.left(int(teta))
        tl.forward(int(L2))
        tl.left(int(teta))
        tl.forward(int(L3))
    

    for i in range (1,3):
        tl.penup()
        tl.goto(0, int(R+b))
        tl.pendown()   

        tl.setheading(270)
        tl.left(30*i)

        tl.penup()
        tl.forward(int(b))
        tl.pendown()

        tl.forward(int(L1))
        tl.right(int(teta))
        tl.forward(int(L2))
        tl.right(int(teta))
        tl.forward(int(L3))

    for i in range (1,3):
        tl.penup()
        tl.goto(0, int(R+b))
        tl.pendown()   

        tl.setheading(180)
        tl.left(30*i)

        tl.penup()
        tl.forward(int(b))
        tl.pendown()

        tl.forward(int(L1))
        tl.left(int(teta))
        tl.forward(int(L2))
        tl.left(int(teta))
        tl.forward(int(L3))



