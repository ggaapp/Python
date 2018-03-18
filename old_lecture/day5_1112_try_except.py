SEPARATOR = '\n' + '__'*20 + '\n\n\n'


def test1_try_except():
    while True:
        _a_str = input('input a string = ')
        _b_str = input('input b string = ')

        try:
            _c = int(_a_str) * int(_b_str)

        except:
            print('Not Number', SEPARATOR)
            continue

        print('%s x %s = %s' % (_a_str, _b_str, _c), end='\n\n\n')
        # print('{:,} x {:,} = {:,}'.format(str(_a_str), str(_b_str), str(_c)))
#test1_try_except()

def test2_try_except_else_finally():
    while True:
        try:
           _a_int = input('input a integer = ')
           _b_int = input('input b integer = ')
        except ValueError:
            print('Input number only \n\n')
            continue

        print('SEE ME? O.K..!!\n\n')

        try:
            _answer = _a_int / _b_int

        except ZeroDivisionError:
            print('Cannot be devided by zero', SEPARATOR)
            continue
        except:
            pass
        else:
            pass
        finally:
            print('You CANNOT count!!! HAHAHA..')
#test2_try_except_else_finally()



""" Built-in Functions
- enumerate, zip, map, lambda, chr, ord
- enumerate(iterator) = i, iterator
- map(f(x), iterator)
- zip(*iterables)
- lambda = oneline function define w/o func_name
- chr('int') <--> ord('str')
- dir(), id(), help(), ..... etc
"""
