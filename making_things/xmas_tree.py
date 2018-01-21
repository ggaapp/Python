import turtle as tu
import random
import math

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

tu.speed('fastest')

def move(pos_x=0, pos_y=0):
    tu.penup()
    tu.setx(pos_x)
    tu.sety(pos_y)
    tu.pendown()

def go(go, angle=0):
    """
    go=forward
    angle=turn: left=minus 180 / right= plus 180
    """
    tu.forward(go)
    tu.right(angle)

def star(pos_x, pos_y, size=10, width=1, trailing=False):
    tu.width(width)
    if trailing:
        tu.setx(pos_x)
        tu.sety(pos_y)
    else:
        tu.penup()
        tu.setx(pos_x)
        tu.sety(pos_y)
        tu.pendown()

    tu.begin_fill()
    tu.left(90+126)
    for i in range(5):
        tu.forward(size)
        tu.right(144)
        tu.forward(size)
        tu.left(72)
    tu.end_fill()
    tu.setheading(0)




def draw_triangle(pos_x, pos_y, lowerside, angle=40, width=10):
    l = lowerside / 2
    radian = math.radians(angle)
    sameside = l/math.cos(radian)
    tu.penup()
    tu.setx(pos_x)
    tu.sety(pos_y)
    tu.width(width)
    tu.color('darkgreen', 'green')
    tu.begin_fill()
    tu.pendown()
    tu.right(angle)
    tu.forward(sameside)
    tu.left(180+angle)
    tu.forward(lowerside)
    tu.left(180+angle)
    tu.forward(sameside)
    tu.right(angle)
    tu.end_fill()
# draw_triangle(pos_x, pos_y, lowerside, angle=40, width=10)
sum=0
for i in range(0, 4):
    sum = sum + i*15
    draw_triangle(0, sum, 400-100*i)
