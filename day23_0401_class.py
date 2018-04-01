# ---방법 1---
import _static.module_custom.class_car as cc

a = cc.SportCar('PORSCHE')

print(a.show_status())
cc.speed_up_down(a)


# ---방법 2---
from _static.module_custom.class_car import *

if __name__ == '__main__':
    a = TruckCar('T')
    b = TruckCar('Bongo')
    c = SportCar('PORSCHE')

    c.attr['max_speed'] = 200
    c.attr['s_able'] = 50

    c.show_status()

    speed_up_down(c)
    speed_up_down(b)


# ---방법 3---
from _static.module_custom.class_car import SportCar, speed_up_down

a = SportCar('PORSCHE')
print(a.show_status())
speed_up_down(a)
