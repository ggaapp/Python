"""
화일 독스트링 : 화일의 설명 - 가위.바위.보 -모듈(블랙박스)
"""
import os
import random

import _script_run_utf8
_script_run_utf8.main()

NUMBER_ATTACKS = 20
DECO_SEPARATOR = "=+" * 15
DRAW = ["-", "가위", "바위", "보ㅡ"]         # POS = 1,2,3 , POS'0'은 버린다.
RESULT = { 1: "승", 0: "패", -1 : "무"}    # 키값 = 1, 0, -1 로 호출한다.

def get_me_com_attacks(length=10):
    """ 가위.바위.보 - 랜덤어택 리스트 갯수'length'만큼을 생성한다.
    # 예: 3개 = [(1,2), (2,3), (1,1)] ... length=3
    """
    return [(random.randint(1, 3), random.randint(1,3)) for n in range(length)]

def get_result_rock_paper_scissors(me, com):
    """ 가위.바위.보 승무패를 판단해 준다.
    # IN = 1,2,3 중 하나, 가위,바위, 보 = me, com
    # OUT = 1,0,-1 중 하나 -- 승무패
    """
    eq = me - com
    if eq == 0:
        return -1       # ? = 무
    elif eq == 1 or eq == -2:
        return 1        # 1, Ture = 승
    elif eq == -1 or eq == 2:
        return 0        # 0, False = 패

def get_stack_win_draw_lose_count(judge, win_cnt, draw_cnt, lose_cnt):
    """ 모듈로 대체하는 구문 : 심판을 받아서, 승-무-패를 누적한다.
    # if judge == 1:
    #     win_count += 1
    # elif judge == 0:
    #     lose_count += 1
    # else:
    #     draw_count += 1
    """
    if judge == 1:
        win_cnt += 1
    elif judge == 0:
        lose_cnt += 1
    else:
        draw_cnt += 1
    return win_cnt, draw_cnt, lose_cnt

def is_stop_ok():
    return input("\n그만 하시겠습니까? (Yes/No=Enter) ").lower().startswith("y")

def select_mode():
    return int(input("모드를 선택하십시오(0-quit/1-infinite loop/2-win test) "))

if __name__ == '__main__':
    mode=select_mode()
    if mode==0: pass
    elif mode==1:
        while True:
            os.system("cls")
            win_cnt, draw_cnt, lose_cnt = 0,0,0
            attacks=get_me_com_attacks(NUMBER_ATTACKS)
            for i, attack in enumerate(attacks, 1):
                (me, com)=attack
                result = get_result_rock_paper_scissors(me, com)
                win_cnt, draw_cnt, lose_cnt = get_stack_win_draw_lose_count(result, win_cnt, draw_cnt, lose_cnt)
                print('{:>2}. {:>2} / {:>2} = {:>1}'.format(i, DRAW[me], DRAW[com], RESULT[result]))
            print('\n\n'+DECO_SEPARATOR+'\n')
            print('{:>2}승 {:>2}무 {:>2}패 ---- {:>2}전 :: 승률 : {:.3f}'.format(win_cnt, draw_cnt, lose_cnt, NUMBER_ATTACKS, win_cnt/NUMBER_ATTACKS))
            if is_stop_ok():
                break
    elif mode==2:
        attempt=0
        while True:
            attempt+=1
            win_cnt, draw_cnt, lose_cnt = 0,0,0
            attacks=get_me_com_attacks(NUMBER_ATTACKS)
            for attack in attacks:
                (me, com)=attack
                result = get_result_rock_paper_scissors(me, com)
                win_cnt, draw_cnt, lose_cnt = get_stack_win_draw_lose_count(result, win_cnt, draw_cnt, lose_cnt)
            print('{:>2}승 {:>2}무 {:>2}패 ---- {:>2}전 :: 승률 : {:.3f}\n'.format(win_cnt, draw_cnt, lose_cnt, NUMBER_ATTACKS, win_cnt/NUMBER_ATTACKS))
            if win_cnt==20:
                break
        print('Success!  Try : %d' % (attempt))
