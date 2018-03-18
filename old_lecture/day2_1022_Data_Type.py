"""
Numbers - Integer : -1, 0, 1, -118276378167 ...
          Float : 0.10223, 0.1203, 3232.234 ...
          Binary : 0b....
          Octa-Decimal : 0o....
          Hexa-Decimal : 0x....

Operators - + : sum
            - : substraction
            * : multiply
            / : division
            ** : power
            % : remainder
            // : quotient
"""
""" (1) Number Type """
def test_1():
  _a = 100
  _b = 3

  _c = _a + _b # = 103

  _d = _a / _b # = 33.3333333 'float'
  _e = _a // _b # = 33 'int'
  _f = _a % _b # = 1 'int'

  print('_a / _b = ', _d)
  print('_a // _b = ', _e)
  print('_a % _b = ', _f)
  print()

  print('ABC', end = '')
  print('ABC', end = '')
  print('ABC', end = '')
  print()

  print('ABC', end = '\n\n\n')
  print('ABC', end = '\n\n\n')
  print('ABC', end = '\n\n\n')
  print()


  print('0b1111 = ', bin(15))
  print('0o17 = ', oct(15))
  print('0xF = ', hex(15))
  print()

  _a = '1'
  int(_a)
  print(type(_a))

  _a = '1.0'
  float(_a)
  print(type(_a))

  _a = 1
  str(_a)
  print(type(_a))
#test_1

""" (2) Text Type : Escape Code & String Cal """
def test_2():
  _a = """wjbfnbdfsd\nwefwjefkojwowef\nwhefbihweifhwef\n"""
  #print(_a)
  _a = '\a'
  print(_a)

  _a = "\aPython's favorite food is perl"
  _a = 'Python\'s \\favoritefood is perl\a'
  #print(_a)

  _a = 'this'
  _b = ' is a book'

  _c = (_a + _b + '\n')*5
  print(_c, '\a')
#test_2

_a = "Life is too short, you need Python"

""" INDEXING (position) """
def test_3():
  print(len(_a))    # 34
  print(_a[0])      # 'L'
  print(_a[33])     # 'n'
#test_3

""" SLICING """
def test_4():
  print(_a[0:4])
  print(_a[28:34])
  print(_a[-6:])
  print(_a[:-6])
  print(len(_a[:-6]))

  _b = "Pithon"
  _b = _b[:1]+'y'+_b[2:]
  print(_b, '\a')
#test_4

""" FORMATTING """
def test_5():
    pass

import random

for n in range(100):
  _a = ['I', 'You', 'My dog', 'God', 'Donald Trump', 'Moon Jae In', 'MB', 'Park Geune', 'Mario', 'Kim Du han']
  _a_num = len(_a) # 'int' 10
  # print(_a_num)
  _a_rand_num = random.randint(1, _a_num)

  _b = ['1','2','3','4','5','6','7','8','9','10']
  _b_num = len(_b) # 'int' 10
  #print(_b_num)
  _b_rand_num = random.randint(1, _b_num)

  _c = ['refrigerators', 'penpinappleapplepen', 'AK-47', 'mad cow', 'air planes', 'apartments', 'dollars', 'Super Mushroom', 'Trump Card', 'grenades', 'Tyre']
  _c_num = len(_c) # 'int' 10
  #print(_c_num)
  _c_rand_num = random.randint(1, _c_num)

  # print('%s ate %s %s' % (_a, _b, _c))
  print('%s ate %s %s\n' % (_a[_a_rand_num - 1], _b[_b_rand_num - 1], _c[_c_rand_num - 1]))
