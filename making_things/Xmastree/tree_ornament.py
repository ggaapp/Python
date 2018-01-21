import turtle as tu
import random
import math

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

tu.speed(0)
tu.screensize(800, 1200)

def move(pos_x=0, pos_y=0):
    tu.penup()
    tu.setpos(pos_x, pos_y)
    tu.pendown()

def go(go, angle=0):
    tu.forward(go)
    tu.right(angle)

def draw_color_bulb(pos_x, pos_y, size=10, width=3, pen='red', fill='yellow'):
    move(pos_x, pos_y)
    tu.width(width)
    tu.color(pen, fill)
    move(pos_x, pos_y-size/2)
    tu.begin_fill()
    tu.circle(size)
    tu.end_fill()

if __name__ == '__main__':
    r_a=random.randint(100, 200)
    r_b=random.randint(200, 400)
    while True:
        size=random.randint(10, 20)
        width=3
        pen=random.choice(COLOR_PICK)
        fill=random.choice(COLOR_PICK)
        if ((r_a % 2==0)and(r_b % 2==0)):
            y=random.randint(0-r_a/2, r_a/2)
            x=random.randint(0-r_b/2, r_b/2)
        elif (r_a%2==0)and(r_b%2==1):
            y=random.randint(0-(r_a)/2, (r_a)/2)
            x=random.randint(0-(r_b-1)/2, (r_b-1)/2)
        elif (r_a%2==1)and(r_b%2==0):
            y=random.randint(0-(r_a-1)/2, (r_a-1)/2)
            x=random.randint(0-(r_b)/2, (r_b)/2)
        else:
            y=random.randint(0-(r_a-1)/2, (r_a-1)/2)
            x=random.randint(0-(r_b-1)/2, (r_b-1)/2)
        draw_color_bulb(x, y, size, width, pen, fill)
