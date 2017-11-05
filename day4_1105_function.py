import math

""" function calculator """

def get_sum_ab(a, b):  # IN=2'int' / OUT='int'
    """ this is sum of a and b
        a = float, b = float """
    return a, b, a + b

def get_mul_ab(a, b):
    """ this is multiple of a and b
        a = 'float', b = 'float' """

    return a, b, a * b

def get_sub_ab(a, b):
    """ this is subtraction of a and b
        a = 'float', b = 'float' """

    return a, b, a-b

def get_div_ab(a, b):
    """ this is division of a and b
        a = 'float', b = 'float' """

    return a, b, a/b

def get_root_a(a):
    """ this is root of a. b can be anything...
        a = float """

    return a, math.sqrt(a)

def get_a_square_b(a, b):
    """ this is value of a square b
        a = 'float', b = 'float' """

    return a, b, a**b


while True:

    _arg1 = input('a : ')
    _arg2 = input('b : ')
    try:
        _kind = int(input(' What? (1=+, 2=x, 3=-, 4=/, 5=root, 6=square) '))
    except(ValueError):
        print('invalid operand!!!\n')
        continue

    if _arg1=='pi' and _arg2=='pi':
        _arg1 = float(math.pi)
        _arg2 = float(math.pi)
    elif _arg1 == 'pi':
        _arg1 = float(math.pi)
        try:
            _arg2 = float(_arg2)
        except(ValueError):
            print('2nd value is unable to change!!!\n')
            continue

    elif _arg2 == 'pi':
        _arg2 = float(math.pi)
        try:
            _arg1 = float(_arg1)
        except(ValueError):
            print('1st value is unable to change!!!\n')
            continue
    else:
        try:
            _arg1 = float(_arg1)
        except(ValueError):
            print('1st value is unable to change!!!\n')
            continue
        try:
            _arg2 = float(_arg2)
        except(ValueError):
            print('2st value is unable to change!!!\n')
            continue



    if _kind == 1:
        operator = '+'
        _a, _b, _c = get_sum_ab(_arg1, _arg2)
        print('%s %s %s = %s\n' % (_a, operator, _b, _c))

    elif _kind == 2:
        operator = 'x'
        _a, _b, _c = get_mul_ab(_arg1, _arg2)
        print('%s %s %s = %s\n' % (_a, operator, _b, _c))

    elif _kind == 3:
        operator = '-'
        _a, _b, _c = get_sub_ab(_arg1, _arg2)
        print('%s %s %s = %s\n' % (_a, operator, _b, _c))

    elif _kind == 4:
        operator = '/'
        _a, _b, _c = get_div_ab(_arg1, _arg2)
        print('%s %s %s = %s\n' % (_a, operator, _b, _c))

    elif _kind == 5:
        operator = 'root'
        _a, _b = get_root_a(_arg1)
        print('%s %s = %s\n' % (operator, _a, _b))

    elif _kind == 6:
        operator = '^'
        _a, _b, _c = get_a_square_b(_arg1, _arg2)
        print('%s %s %s = %s\n' % (_a, operator, _b, _c))
