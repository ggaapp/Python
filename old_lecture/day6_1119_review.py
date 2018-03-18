
SEPERATOR = '\n' + '__'*30 + '\n\n'

def test1_chr_ord():
    """ ASCii keyboard = 32 ~ 125
     - function CHR('int') <--> ORD('str')
    """
    print('a = ', ord('a'))               #97
    print('A = ', ord('A'), SEPERATOR)    #65

    print('chr(97) = ', chr(97))
    print('chr(65) = ', chr(65), SEPERATOR)
# test1_chr_ord()

def test2_ascii():
    counter = 1
    for n in range(3, 128):
        if n == 8:
            continue
        if n == 9:
            continue
        if n == 10:
            continue
        if n == 13:
            continue
        if n == 27:
            continue
        if counter % 5 == 0:
          print('%5s=%3s' % (n, chr(n)), end = '\n')
          counter = counter + 1
        else:
          print('%5s=%3s' % (n, chr(n)), '\t', end = '')
          counter = counter + 1
# test2_ascii()

MENU_DICT = {
    1:['black noodle', 5500],
    2:['red noodle', 8000],
    3:['tangsuyuk', 10000],
    4:['sprite', 1500],
    5:['polar bear', 1000000000000000000]
}
MENU_FORMAT = """
-----------------------------------------------------------------------
                      MENU-FAN  /  Yun's Restaurant
-----------------------------------------------------------------------
"""

# print(type(MENU_DICT))
# print(MENU_DICT)

print(MENU_FORMAT)
for n in range(1, 6):
    print('  {:}. {:<15}....................{:>26,} won\n'.format(n, MENU_DICT[n][0], MENU_DICT[n][1]))
print('\n-----------------------------------------------------------------------')
