import os
import time
import datetime
import math
""" Refer : DATETIME module Documentation
  - format here : https://docs.python.org/2/library/datetime.html
  (1) datetime, time module
  (2) recursive functions - countdown, factorial, fibonacci(yield)
  (3)
"""

def datetime_module():
    while True:
        _time = datetime.datetime.now()
        # print(_time)
        # print(type(_time))

        ampm = _time.strftime('%p')
        hour = _time.strftime('%H')
        minute = _time.strftime('%M')
        second = _time.strftime('%S')
        weekday = _time.strftime('%A')

        # print(ampm + '  ' + hour + ' : ' + minute + ' : ' + second + ' - ' + weekday)
        _time_format = _time.strftime('%p %H : %M : %S - %Y %A %B %d')
        print(_time_format)
        time.sleep(0.8)
        os.system('cls')
#datetime_module()

""" countdown """
def countdown_normal(start_number):
    for n in range(start_number, -1, -1):
        print(n)
        time.sleep(0.2)
# countdown_normal(10)

def countdown_recursive(start_number):
    if start_number >= 0:
        print(start_number)
        time.sleep(0.2)
        countdown_recursive(start_number-1)
    else:
        print('Fire!')
# countdown_recursive(10)


def factorial(n):
    """ FACTORIAL = 5! = 5 * 4* 3 * 2 * 1
    GF(3) = 3 * GF(2)
                2 * GF(1)
                     1
    there for, GF(4) = 4 * 3 * 2 * 1
    """
    if n != 1:
        return n * factorial(n-1)
    else:
        return 1
#factorial(n)

def print_factorial(n):
    _expression = str(n)
    _value = factorial(n)

    for i in range(n-1, 0, -1):
        _expression += ' x ' + str(i)
    print('{}! = {} = {:,}'.format(n, _expression, _value))
#print_factorial(997)

def fibonacci(n_th):
    if n_th == 1 or n_th == 2:
        return 1
    else:
        return fibonacci(n_th-1) + fibonacci(n_th-2)
#fibonacci(n_th)

def fibo_n_golden_ratio_cmp(n):
    gr = (1+math.sqrt(5))/2
    for i in range(1, n):
        fr = fibonacci(i+1)/fibonacci(i)
        print('{:<3}= {:<12,} fibo_ratio : {:<20} --> ratio : {:<20}'.format(i, fibonacci(i), fr, fr/gr))
# fibo_n_golden_ratio_cmp(100)


import turtle

class NinjaTurtle(object):
    def turtle_go(self, go, left=0, right=0):
        turtle.forward(go)
        turtle.left(left)
        turtle.right(right)

_a = NinjaTurtle()
_b = NinjaTurtle()

# _a.turtle_go(100, 90, 0)
# _a.turtle_go(50, 0, 90)

_b.turtle_go(200, 0, 90)
_b.turtle_go(100, 90, 0)
turtle.mainloop()
# turtle.forward(100)
# turtle.left(90)
#
# turtle.forward(100)
# turtle.left(90)
#
# turtle.forward(100)
# turtle.left(90)
#
# turtle.forward(100)
# turtle.left(90)
#
# turtle.mainloop()
