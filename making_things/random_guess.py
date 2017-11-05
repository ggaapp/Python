import random
import time
""" random function drill
(1) random.randint()
(2) random.choice()
(3) random.shuffle()
"""

def test1_dirtest():
    print(dir(random))

    for n in dir(random):
        print(n)
#test1_dirtest()

def test2_randint():
    """ randint """
    for n in range(30):
        _a = random.randint(0, 10)
        print(_a)
#test2_randint()


def test3_randchoice():
    _a = random.choice('abcdefg')
    _a = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    # _a = random.choice({1:'a', 2:'b', 3:'c'})  # KeyError
    # _a = random.choice({'a':1, 'b':2, 'c':3})  # KeyError
    print(_a)
#test3_randchoice()



def test4_randshuffle():
    _a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    _a = [n for n in range(10) if n/1 == n]  # comprehension list.
    # line 31 = line 32

    for n in range(10000):
        random.shuffle(_a)
        print(_a)
#test4_randshuffle()

def test5_13thFriday():
    while True:
        _a_str = input('Guess number = ')
        print(_a_str)
        if _a_str == '13':
            print('Friday the 13th.--- ok out')
            break
        time.sleep(0.5)
#test5_13thFriday()

def update_log(a, b):
    a.append(b)

while True:

    num_int = random.randint(100, 999)
    real_int = random.randint(1, num_int)

    while True:
        chksum_TF_int = -1
        chk_str = ''

        cnt_int = 1
        ans_list = []

        print('_'*50)
        print('I have a number out of 1~%d.. GUESS!     :' % num_int, end='')


        ans_str = input()

        try:
            if int(ans_str):
                print('CHK=OK numeric!!')
                chksum_TF_int += 1
            else:
                print('CHK=NG... not numeric Error...')



            if int(ans_str)<=num_int:
                    print('CHK=OK... in range!!')
                    chksum_TF_int += 1
            else: print('CHK=NG... out of range Error...')


            print('_'*20)

            if chksum_TF_int==1:
                chk_str = 'True'
            else: chk_str = 'False'

            print('The Answer is....  %s' % ans_str)
            print('The CHECKSUM is....  %s, %d th trial' % (chk_str, cnt_int), end='\n\n\n\n')


        except ValueError:
            print('CHK=NG... not numeric Error...')
            print('CHK=NG... out of range Error...')
            print('_'*20)
            print('The Answer is....  %s' % ans_str)
            print('The CHECKSUM is....  False, %d th trial' % cnt_int, end='\n\n\n\n')
        cnt_int += 1
        if chk_str == 'True':
            ans_int = int(ans_str)
            if ans_int < real_int:
                print('NO!!..xxxxx')
                print('The Guess is smaller than my number..')
                update_log(ans_list, ans_int)
            elif ans_int > real_int:
                print('ooooo')
                print('OOPS!.. The Guess is greater than my number..')
                update_log(ans_list, ans_int)
            elif ans_int == real_int:
                print("Huh?.. BULL'S EYE!!!.. My number is... %d" % real_int)
                print('ANSWER = ', end = '')
                update_log(ans_list, ans_int)
                print(ans_list)
                print('\n\n\n\n')
                retry_str = input('Try again (y/n)??')
                if retry_str == 'n':
                    break
    break
