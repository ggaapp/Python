#! python
import os
import sys
import datetime
""" OPEN A RESTAURANT : Making Order System
  (1) to Show MENU_PAN = MENU_PAN (changeable)
  (2) to Input order = by Item index & quantity
  (3) to Calculate Bills = Including (Tax= 6.5%, Tip= 10%)
"""
NOW = datetime.datetime.now().strftime('%p %H:%M:%S - %A')
SEPARATOR = '\n' + '__'*30 + '\n\n'
MENU_DICT = {
    1 : ['BLACK_NOODLE', 5000],
    2 : ['RED_NOODLE', 7000],
    3 : ['FRIED_DUMPLINGS', 3000],
    4 : ['ROLLED_RICE', 4000],
    5 : ['TTUK-BOK-KI', 3000],
    6 : ['SPRITE(7-UP)', 1000],
    7 : ['BOTTLED_WATER', 500],
    8 : ['POLAR_BEAR', 1]}

MENU_PAN_FORMAT = ""                                +\
    "---------------------------------------------------------\n" +\
    "              MENU-PAN  / Onito's Restautant             \n" +\
    "---------------------------------------------------------\n" +\
    "%s"                                            +\
    "---------------------------------------------------------\n"

BILL_FORMAT = ""                                    +\
    "------------------------------------------------------------\n" +\
    "              $$$ BILL / Yun's Restautant $$$               \n" +\
    "------------------------------------------------------------\n"

def show_menu_pan():
    """ MAKING MENU_PAN in YOUR RESTAURANT """
    MENU_STRING = ''
    for key in MENU_DICT.keys():            # use .keys() .values() .items()
        MENU_STRING += '{:>2}. {:<16} {:.^10} {:5,} won'.format(
            key,
            MENU_DICT[key][0],
            '.',
            MENU_DICT[key][1]) + '\n'
    print(MENU_PAN_FORMAT %MENU_STRING)
    print(NOW)
# show_menu_pan()


def get_input_str():
    input_msg='' +\
      'Please, order menu by index-quantity & space\n' +\
      '(Ex: 1-2 2-1 3-2... just once for each index)  :\n'
    menu_order_str = input(input_msg)
    return menu_order_str
#get_input_str()


menu_order_str = get_input_str()

order_list = menu_order_str.strip().split()
order_dict = {}

for order in order_list:
    try:
        _value=int(order.strip().split('-')[1])
        _key = int(order.strip().split('-')[0])
        order_dict[_key]=_value
    except:
        print('Did you write in format?')
        os.system('pause')
print('\n\n\n\nYOUR ORDER = {0:}'.format(order_dict))
print(BILL_FORMAT)
menu_total = 0
print('ORDER TIME : ' + NOW + SEPARATOR)
for i, key in enumerate(order_dict.keys()):
    _item = MENU_DICT[key][0]
    _price = MENU_DICT[key][1]
    _quantity = order_dict[key]
    _total = _price * _quantity
    print('{}. {:<16}  {:>5,} x {:<8} = {:>15} won'.format(i+1, _item, _price, _quantity, _total))
    menu_total += _total
print(SEPARATOR, end='')
print('MENU TOTAL : {:>40} won'.format(menu_total))
print('TAX : {:>47} won'.format(int(menu_total*0.065)))
print('TIP : {:>47} won'.format(int(menu_total*1.065*0.1)), end='')
print(SEPARATOR, end='')
print('TOTAL BILL : {:>40} won'.format(int(menu_total*1.065*1.1)))
print('PAY AMOUNT : {:>40}00 won'.format(int(int(menu_total*1.065*1.1)/100)), end='')
print(SEPARATOR, end='')
print('THANK YOU\n')
