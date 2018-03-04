""" 포괄적 리스트(Comprehensive List) """
numbers = [n for n in range(1,11)]
yes5 = ["YES" for n in range(5)]
yes5_if = ["YES" for n in range(10) if n%2==0]
yes_no_10 = ["YES" if n%2==0 else "NO" for n in range(1,11)]

yes_vari = 10 if yes_no_10[0] == "YES" else "WHAT?"

# print(numbers)
# print(yes5)
# print(yes5_if)
# print(yes_no_10)
# print(yes_vari)
""" RESULT
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 ['YES', 'YES', 'YES', 'YES', 'YES']
 ['YES', 'YES', 'YES', 'YES', 'YES']
 ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
 WHAT?"""

def get_result_rock_paper_scissors(my, com):
    """가위바위보 결과 전해드립니다
    # IN = 1-'rock', 2-'scissors', 3-'paper'
    # OUT = 1-승, 0-무, -1-패
    """
    if my==com: return '무'
    elif not(my-com-1)%3: return '패'
    elif not(my-com+1)%3: return '승'

def is_playing_stop():
    """
    #더 할거냐고 물어보고 예/아니오를 입력받는다
    #참/거짓을 반환한다
    """
    _a_str = input('Continue?(y/n) ')
    if _a_str.lower().startswith('n'): return True
    else: return False

import random as rnd
import os

chr_dict = {'rock':1, 'scissor':2, 'paper':3}
DECO_SEPARATOR = '-'*40
atmpt = 0
win_count = 0

print('***This is a RockScissorPaper game***\n')
print(DECO_SEPARATOR)
while True:
    me = rnd.randint(1, 3)#input('Enter rock or scissor or paper : ')
    com = rnd.randint(1, 3)
    print('\n'+get_result_rock_paper_scissors(me, com)+'\n\n')
    if get_result_rock_paper_scissors(me, com)=='승': win_count+=1
    atmpt+=1
    if is_playing_stop():
        print(DECO_SEPARATOR)
        break
    print(DECO_SEPARATOR)
os.system('cls')
print('\n'*8+'You did %d games.. Winnig Rate : %.3f' % (atmpt, win_count/atmpt))
