def test1_sum_and_avg():
    lit = int(input('국어 성적을 입력하세요 : '))
    math = int(input('수학 성적을 입력하세요 : '))
    eng = int(input('국어 성적을 입력하세요 : '))
    sc_sum = lit+math+eng
    sc_avg = sc_sum/3
    print('\n입력받은 성적\n--------------------\n' +
    '국어 성적 : {}\n수학 성적 : {}\n영어 성적 : {}\n\n'.format(lit, math, eng))
    print('--------------------\n\n' + '총점 : {}\n평균 : {:.2f}'.format(sc_sum, sc_avg))
# test1()

def test2_celcius_to_farenheit():
    exp = """This program convert celcius to\nFarenheit degree temperature.\nInput C.degree which want to be converted\n"""
    print('='*50 + '\n' + exp + '-'*50)
    while True:
        cel = float(input('INPUT TEMP : '))
        print('* Dom. Eg : F.degree = ((9/5) * C.degree) + 32\n')
        far = ((9/5) * cel) + 32
        print('\t(1) Celcius.D : {}˚C\n\t(2) Farenheit.D : {:.2f}˚F'.format(cel, far))
        print('-'*50)
        again = input('Quit?(y/n) : ')
        if again!='y' or again!='n':
            print('Error Occured!')
            exit(-1)
        elif again=='y':
            print('\n'*3)
        elif again=='n':
            quit()
# test2_celcius_to_farenheit()

def test3_circle():
    pi = 3.141592
    r = int(input('Enter radius : '))
    d = 2*pi*r
    s = pi*(r**2)
    print('Radius : {:>29}'.format(r))
    print('Area of circle : {:21.3f}'.format(s))
    print('Perimeter of circle : {:16.3f}'.format(d))
# test3_circle()

def test4_5digit():
    num = int(input('Enter a 5 digit number : '))
    print('{1}, {2}, {3}, {4}, {5}'.format(n//10000, (n%10000)//1000, (n%1000)//100, (n%100)//10, n%10))
# test4_5digit()

import random
def test5_random_multiple():
    n = random.randint(1000, 10000000)
    k = random.randint(10000, 10000000)
    n_step = random.randint(100000, 10000000)
    k_step = random.randint(100000, 100000000)
    n_range = random.randint(10000, 1000000000)
    k_range = random.randint(100000, 10000000000)
    for r_n in range(n, n_range, n_step):
        for r_k in range(k, k_range, k_step):
            print('{:>10,} X {:>10,} = {:>20,}'.format(r_n, r_k, r_n*r_k))
# test5_random_multiple()

def test5_random_multiple2():
    while True:
        n = random.randint(10, 100000000000000000000000)
        k = random.randint(7, 30)**random.randint(5, 20)
        print('{:>30,} X {:>40,} = {:>70,}'.format(n, k, n*k))
test5_random_multiple2()
