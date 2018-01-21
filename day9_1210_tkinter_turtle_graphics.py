""" TELETYPE :
  - DAY09_1211_tkinter_tu.py
  - DOCUMENTATION : https://docs.python.org/3.3/library/tu.html?highlight=turtle

  노랑 : 준혁
  주황 : 준하
  파랑 : 쌤
  초록 : 지용
"""

import turtle as tu
import random
import math

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']
SCREEN_X = 470
SCREEN_Y = 400

tu.speed(10)
tu.shape('turtle')

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

def test1_simple_filled_tiangle():
    _pen = random.choice(COLOR_PICK)
    _fill = random.choice(COLOR_PICK)
    # tu.color('blue','yellow') # pen, fill-color
    tu.color(_pen, _fill) # pen, fill-color
    tu.width(5)

    tu.begin_fill()

    tu.forward(100)
    tu.left (90)
    tu.forward(100)
    tu.right(90)
    tu.setx(0)
    tu.sety(0)

    tu.end_fill()

# for n in range(36):
#     test1_simple_filled_tiangle()
#     go(0,10)
#
# tu.color('red','yellow')
# star(0, 0, size=50, width=5)
# star(-200, -200, size=50, width=5)
# star(-200, 200, size=50, width=5)

import turtle as tu

_b = tu.Turtle()
_b.speed(0)


COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

_b.speed('fastest')

def move(obj, pos_x=0, pos_y=0):
    obj.penup()
    obj.setx(pos_x)
    obj.sety(pos_y)
    obj.pendown()

def go(obj, go, angle=0):
    """
    go=forward
    angle=turn: left=minus 180 / right= plus 180
    """
    obj.forward(go)
    obj.right(angle)

go(_b, 100, 90)
go(_b, 100, -90)

go(_b, 100, 90)
go(_b, 100, -90)

go(_b, 100, 90)
go(_b, 100, -90)

_a = tu.Turtle()
_a.color('red','green')
_a.width(10)

go(_a, 100, -90)
go(_a, 100, 90)

go(_a, 100, -90)
go(_a, 100, 90)

go(_a, 100, -90)
go(_a, 100, 90)


_c = tu.Turtle()
_c.color('blue','green')
_c.width(10)

go(_c, 50, -90)
go(_c, 50, 90)

go(_c, 50, -90)
go(_c, 50, 90)

go(_c, 50, -90)
go(_c, 50, 90)

tu.mainloop()
