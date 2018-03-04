# Beginner
""" 문제 1 : 0~n까지 input()을 받아서 더해라 """
def test1():
    n=int(input('몇까지 더할까요? : '))
    sum = int(n*(n+1)/2)
    print('정답은 {} 입니다'.format(sum))
# test1()

""" 문제 2 : 좌우로 0.2초 씩 움직이는 헬로월드 """
import time
import os

def test2():
    # |[Hello]----------| WORLD!
    string = ['-' for i in range(11)]
    insert = '[Hello]'
    last = 'WORLD!'
    while True:
        for n in range(11):
            string[n]=insert
            insert_string=''.join(string)
            print('|'+insert_string+'|'+last)
            string[n]='-'
            time.sleep(0.2)
            os.system('cls')
        for n in range(9, 0, -1):
            string[n]=insert
            insert_string=''.join(string)
            print('|'+insert_string+'|'+last)
            string[n]='-'
            time.sleep(0.2)
            os.system('cls')
# test2()

""" 문제 3 : 자료 3개의 딕셔너리 키값, 밸류값을 프린트 해라 """
def test3():
    sample_dict = {1:'집', 2:'우산', 3:'자동차'}
    print('키값에는 {} = {}개의 자료가 있습니다.')
    print('형식은 {} 입니다.')
    print('\n')
    print('밸류값에는 {} = {}개의 자료가 있습니다.')
    print('형식은 {}입니다.')
# test3()
