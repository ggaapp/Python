from making_things.Xmastree.tree_ornament import *
tu.screensize(500, 900)
def star(pos_x, pos_y, size=10, width=3):
    tu.color('red','yellow')
    move(pos_x, pos_y)
    tu.width(width)
    tu.begin_fill()
    tu.left(90+126)
    for i in range(5):
        tu.forward(size)
        tu.right(144)
        tu.forward(size)
        tu.left(72)
    tu.end_fill()
    tu.setheading(0)
def tree_trunk(pos_x, pos_y, forward, width=10):
    tu.setheading(0)
    tu.setpos(pos_x, pos_y)
    tu.width(width)
    tu.pencolor('brown')
    tu.right(90)
    tu.forward(forward)
    tu.setheading(0)
def draw_triangle(pos_x, pos_y, lowerside, width=5, angle=40):
    l = lowerside / 2
    radian = math.radians(angle)
    sameside = l/math.cos(radian)

    tu.color('darkgreen', 'green')
    tu.width(width)
    move(pos_x, pos_y)

    tu.begin_fill()
    tu.right(angle)
    tu.forward(sameside)
    tu.left(180+angle)
    tu.forward(lowerside)
    tu.left(180+angle)
    tu.forward(sameside)
    tu.right(angle)
    tu.end_fill()
def main():
    star(0, 165, 20, 10)
    tree_trunk(0, 130, 310, 20)

    draw_triangle(0, 150, 125)
    draw_triangle(0, 115, 175)
    draw_triangle(0, 60, 250)
    draw_triangle(0, 0, 325)

    pos_x = [165, 125, 90, 62.5,
        -165, -125, -90, -62.5,]
    pos_y = [-155, -65, 20, 80,
        -155, -65, 20, 80,]
    pos_xy = list(zip(pos_x, pos_y))

    for posxy in pos_xy:
        fill = random.choice(COLOR_PICK)
        draw_color_bulb(posxy[0], posxy[1], 10, 2.5, 'red', fill=fill)
if __name__ == '__main__':
    for n in range(1000):
        x=random.randint(-500, 500)
        y=random.randint(-450, 450)
        tu.pencolor('darkgray')
        size=random.randint(1, 3)
        move(x, y-size/2)
        tu.circle(size)
    main()
    move(0, -270)
    tu.write('MERRY CHRISTMAS\n & HAPPY NEW YEAR',
        font=('Calibri', 28, 'bold'),
        align='center')
    tu.mainloop()
