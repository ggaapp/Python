""" Everything of 객체
 - *** Attribute(값) / Method(속성)
 - 객체의 종류(type)와 위치주소(id)
 - 들여다보기 : 기능 나열(dir) - 디렉토리의 약자
 - 객체 전체 오버뷰(둘러보기) - help
"""


def show_id(_a, _b, _c):
    """ 함수의 인자 = 파라미터 / 파라미터 --> 내부변수에 전달 (지역변수)
    - 파라미터와 내부변수는 다르다 / 함수가 닫히면 내부변수(지역변수)는 사라진다.
    """
    print()
    # print('_a =', id(_a), '-->', _a)
    print('_a = {} --> {}'.format(id(_a), _a))
    print('_b = {} --> {}'.format(id(_b), _b))
    print('_c = {} --> {}'.format(id(_c), _c))

def test1():
    """ # 숫자는 불변객체 () 테스트 """
    a=100
    b=200
    c=a

    show_id(a, b, c)

def test2():
    """ # 리스트 객체 테스트 """
    d=[1,2,3,4]
    e=[1,2,3,4]
    f=d

    show_id(d,e,f)

    f=d.copy
    d.append(5)

    show_id(d,e,f)

def stop():
    print('더 이상 벽에는 맥주가 없네~, 더 이상 벽에는 맥주가 없네~')
    ck = input('더 하시겠습니까?(y=Enter/n) ')
    return ck.lower().startswith('n')

import time

def test3(beer_num, cnt=1):
    for n in range(beer_num):
        if n==beer_num-1:
            print('1병의 맥주가 벽에 있네~, 1병의 맥주가 벽에 있네~\n 이제 한병을 내려 마셨네~, ..............\n',flush=True)
            if stop():
                print('\n\n\n네가 마신 맥주병 개수 : %d ~~~~~ 술 좀 그만 쳐 마셔대라 이 술고래 자식아!!' % (beer_num*cnt))
                break
            else:
                cnt+=1
                print('\n\n더 이상 벽에는 맥주가 없네~, 더 이상 벽에는 맥주가 없네~\n가게에 나가서 맥주를 사왔네, 99병의 맥주들이 벽에 있네~\n\n',flush=True)
                test3(beer_num, cnt=cnt)
        else:
            print('%d병의 맥주들이 벽에 있네~, %d병의 맥주들이 벽에 있네~\n 이제 한병을 내려 마셨네~, %d병의 맥주들이 벽에 있네~\n' % (beer_num-n, beer_num-n, beer_num-n-1), flush=True)
        time.sleep(0.2)
test3(1)
