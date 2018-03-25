""" 문제. A-1 편의점 물건을 계산하라
# 편의점 카운터에서 물건코드를 숫자(int)을 입력받은 후 최종가격을 알려주는 SW
# 가격DB는 3개만 딕셔너리 / 손님은 'item-갯수' 1-1 2-1 3-1 spc구분으로 입력
# 가장 심플한 영수증을 출력한다. (단, input구문은 테스트 CASE로 처리할 것!)
# input_str = input("번호-수량(공백)으로 입력 :")
# input_str = "1-1 2-2 3-1"
    빵ㅡ   : 1 x 1,000 = 1,000
    우유   : 2 x 2,000 = 4,000
    계란   : 1 x   500 =   500
    ------------ 합계: 5,500원
"""
PRICE_DICT = {
    1: ("빵ㅡ", 1000),
    2: ("우유", 2000),
    3: ("계란", 500)}

def test_A1():
    order = input('주문 : ')
    ord_list = order.split(' ')
    for ord in ord_list:
        ord = ord.split('-')

    sum=0
    for orders in ord_list:
        (name, price)=PRICE_DICT[int(orders[0])]
        count=int(orders[2])
        print('{}   : {} x {:>5,} = {:>5,}'.format(name, count, price, count*price))
        sum+=count*price
    print('-'*12 + ' 합계 : {:5,}원'.format(sum))
#test_A1()

""" 문제. A-2 (1+1)할인 기간을 반영하라 (할인모드1)
# 평상 시에는 일반적인 편의점 계산 영수증 --> (A-1 코드 '복+붙' 후 수정)
# sale_mode = 1 일때는, 2개 사면 1개 더 주는 이벤트 모드 돌입 (2+1)
# 영수증 가격 옆에 (+'n'개 더!)만 추가로 반영한다. / 항목에 index번호도 추가(!)
    1.빵ㅡ   : 1 x 1,000 = 1,000
    2.우유   : 4 x 2,000 = 8,000 (+2개 더!)
    3.계란   : 1 x   500 =   500
    ------------ 합계: 9,500원
    * 2+1 이벤트 기간 중 입니다.
"""

def test_A2():
    order = input('주문 : ')
    ord_list = order.split(' ')
    for ord in ord_list:
        ord = ord.split('-')

    sum=0
    sale_mode = 1
    how_much = 1
    for orders in ord_list:
        (name, price)=PRICE_DICT[int(orders[0])]
        count=int(orders[2])
        if sale_mode != 0:
            if count // sale_mode:
                plus = (count // sale_mode)*how_much
                print('{}   : {} x {:>5,} = {:>5,} (+{}개 더!)'.format(name, count+plus, price, count*price, plus))
        else: print('{}   : {} x {:>5,} = {:>5,}'.format(name, count, price, count*price))
        sum+=count*price
    print('-'*12 + ' 합계 : {:5,}원'.format(sum))
    if sale_mode != 0:
        print('* {}+{} 이벤트 기간 중 입니다.'.format(sale_mode, how_much))
#test_A2()
