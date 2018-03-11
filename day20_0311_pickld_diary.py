""" '피클'드 게시판 글쓰기
- pickle.load(f) : 객체(f)를 읽어서 올린다.
- pickle.dump(data, f) : 객체(f)에 데이터(data)를 덤프한다.
- week_num = datetime.date(2018, 06, 12).weekday() : 요일
"""

import time
import datetime
import pickle
import os

def test1():
    n=1
    while n<=30:
        if n%3==0 and n%5!=0:
            print('에취')
        elif n%5==0 and n%3!=0:
            print('쿨럭')
        elif n%5==0 and n%3==0:
            print('딸꾹딸꾹')
        else: print(n)
        time.sleep(0.7)
        n+=1
# test1()

def g369():
    n=33333333333333333333333333333333333333333333333333333333333333333333333333
    while n>=1:
        printing_number = ''
        for k in str(n):
            if '3' in k or '6' in k or '9' in k:
                printing_number+='짝'
        if printing_number=='':
            print(n)
        else: print(printing_number)
        printing_number=''
        time.sleep(0.05)
        n+=1
# g369()


import _script_run_utf8
_script_run_utf8.main()

FILENAME_WITH_DIR = "./_static/_pickle/pickled_dict.pck"

BOARD_DICT = {
20180311:
""" 제일 첫번째가 제목
다음부터는 게시글 내용 1
이렇게 사용합니다
""",
20190311:
""" 제일 첫번째가 제목
다음부터는 게시글 내용 2
이렇게 사용합니다
""",
20200311:
""" 제일 첫번째가 제목
다음부터는 게시글 내용 3
이렇게 사용합니다
""",
20210311:
""" 제일 첫번째가 제목
다음부터는 게시글 내용 4
이렇게 사용합니다
""",
20220311:
""" 제일 첫번째가 제목
다음부터는 게시글 내용 5
이렇게 사용합니다
"""
}
def write_pickle(filename_with_dir, data):
    with open(filename_with_dir, 'wb') as f:
        pickle.dump(data, f)

def read_pickle(filename_with_dir):
    with open(filename_with_dir, 'rb') as f:
        return pickle.load(f)

# write_pickle(FILENAME_WITH_DIR, BOARD_DICT)

BOARD_DICT = read_pickle(FILENAME_WITH_DIR)


def show_detail_view(board_dict, key):
    os.system("cls")
    key_str = str(key)
    year, month, day = key_str[:4], key_str[4:6], key_str[6:]
    title = board_dict[key].split('\n')[0]
    content = board_dict[key].replace( title+'\n', '')
    print('%s(%s.%s.%s)' % (title, year, month, day))
    print('------------------------------------------')
    print('%s' % (content))
    print('------------------------------------------')
    input('돌아가기=엔터')
    os.system("cls")
    show_board_list(BOARD_DICT)
    
def show_board_list(board_dict):
    print("데이터 : ('%d건')" % len(board_dict))
    print("----------------------------------------------")
    print("번호....날짜......[제.....목]...............")
    print("----------------------------------------------")
    for i, key in enumerate(board_dict, 1):
        title = board_dict[key].split('\n')[0]
        print("%d. [%s] - %s" % (
            i,
            key,
            title
        ))
    print("----------------------------------------------")
    print(":입력 키값: (V)eiw / (A)dd / (Q)uit -- (양식 : 명령 날짜)")
# show_board_list(BOARD_DICT)

while True:
    show_board_list(BOARD_DICT)

    order = input('>')

    if order[0].upper().startswith('V'):
        key = int(order.split(' ')[1])
        try:
            show_detail_view(BOARD_DICT, key)
        except(KeyError):
            os.system("cls")
            input('404 Not Found')
            os.system("cls")
    elif order[0].upper().startswith('A'):

    else:
        print('403 Forbidden')
