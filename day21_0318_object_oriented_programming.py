""" 클래스 객체/오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
  ** 함수형 프로그래밍 / 객체지향 프로그래밍 = 파이썬 특징의 2축!
  : 클래스 객체 = 흔히 붕어빵 틀(클래스) <--> 붕어빵(인스턴스)에 비유한다.
  :   붕어빵 틀은 1개 인데, 팥-붕어빵, 크림-붕어빵, 다양한 변종을 찍어낸다.
  :   찍어 낸 (인스턴스)는 독립적으로 작동 한다(self)

 1.클래스명 작명 = 파스칼 케이스 (ThisIsPascalCase)
 - 클래스 함수(매서드)의 첫번째 인자 = 인스턴스 자신(Self)
 - 클래스간 띄어쓰기는 2칸 / 함수(매서드)는 1칸 이다.

 2.오브젝트(객체)의 특징! : 클래스 오브젝트 <--> 인스턴스
 - (1) 값 (field) = 클래스변수 or 인스턴스 변수
 - (2) 기능 (method) = 매서드, 매직매서드, 더블언더스코어

 3.클래스만의 매우 특별한 기능
  * 상속 (Inherit) = 부모(Parent) - 자식(Child)
  * 중복 (Override) = 덮어쓰기 / 겹쳐쓰기

 4.'매직 매서드' = '더블 언더스코어' __무엇__ ... '매직' + '매서드' = 뭔가 특별한.
  * 자주쓰는 '매직'
  - __init__ (생성자)  <-->  __del__ (소멸자)
  - __repr__, __str__  : 스트링을 '리턴'
  - __add__, __sub__ ... '연산자'
"""
# import _script_run_utf8
# _script_run_utf8.main()

""" 만 들려는 매서드, 클래스변수, 인스턴스변수(self)
값 = 클래스변수(성격), 인스턴스변수(이름, 개인비밀)
기능 = 생성자, 소멸자, 연산자
"""


class Human(object):
    total_count = 0
    icon = '무던'
    motto = ''
    number = 0
    nick = ''
    job = ''
    vote=0

    def say_hello(self):
        print("Hello, I'm %s" % (self.name))

    def campaign(self):
        print("%s 기호 %d번 %s" % (self.motto, self.number, self.name))

    def intro(self):
        print('%s한 %s, %s' % (self.icon, self.nick, self.name))

    def speech(self):
        print('%s : %s' % (self.name, self.motto))

    def say_status(self):
        print("'{}'님의 성격은 '{}'이고, 직업은 '{}'입니다.".format(self.name, self.icon, self.job))

    def __init__(self, name):
        Human.total_count+=1
        self.name = name

    def __add__(self, obj):
        print('{}와 {}는 결혼했습니다.'.format(self.name, obj.name))

    def __sub__(self, obj):
        print('{} 와 {}는 이혼했습니다.'.format(self.name, obj.name))

    def __del__(self):
        print('{}는 죽었습니다.'.format(self.name))


class ManOne(Human):
    pass

def world1():
    man = Human('문재인')
    man.motto = '사람이 먼저다'
    man.job = '정치인'
    man.number=1
    man.campaign()

    swings = Human('스윙스')
    swings.motto = '짬에서 나오는 바이브'
    swings.icon = '컹스'
    swings.nick = '돈가스'
    swings.job = '래퍼'
    swings.number = 2
    swings.intro()
    swings.speech()

    woman = Human('탕웨이')
    woman.motto = '놓치지 않을 거예요'
    woman.job = '배우'
    woman.number = 3
    woman.speech()

    MB = Human('MB')
    MB.motto = '이거 다 거짓말인거 아시죠?'
    MB.job = '전 대통령'
    MB.number = 4
    MB.speech()

    ahn = Human('Ahn철수')
    ahn.job = '정치인'
    ahn.motto = '대한민국 바꿀 사람 누굽니까!!!!'
    ahn.number = 5
    ahn.campaign()



    hu1 = Human('인간1')
    hu2 = Human('인간2')
    hu3 = Human('인간3')
    hu4 = Human('인간4')
    hu5 = Human('인간5')
    hu6 = Human('인간6')
    hu7 = Human('인간7')
    hu8 = Human('인간8')
    hu9 = Human('인간9')
    hu10 = Human('인간10')
    hu11 = Human('인간11')
    hu12 = Human('인간12')
    hu13 = Human('인간13')
    hu14 = Human('인간14')
    hu15 = Human('인간15')
    hu16 = Human('인간16')
    hu17 = Human('인간17')
    hu18 = Human('인간18')
    hu19 = Human('인간19')
    hu20 = Human('인간20')
    hu21 = Human('인간21')
    hu22 = Human('인간22')
    hu23 = Human('인간23')
    hu24 = Human('인간24')
    hu25 = Human('인간25')
    hu26 = Human('인간26')
    hu27 = Human('인간27')
    hu28 = Human('인간28')
    hu29 = Human('인간29')
    hu30 = Human('인간30')
    hu31 = Human('인간31')
    hu32 = Human('인간32')
    hu33 = Human('인간33')
    hu34 = Human('인간34')
    hu35 = Human('인간35')
    hu36 = Human('인간36')
    hu37 = Human('인간37')
    hu38 = Human('인간38')
    hu39 = Human('인간39')
    hu40 = Human('인간40')
    hu41 = Human('인간41')
    hu42 = Human('인간42')
    hu43 = Human('인간43')
    hu44 = Human('인간44')
    hu45 = Human('인간45')
    hu46 = Human('인간46')
    hu47 = Human('인간47')
    hu48 = Human('인간48')
    hu49 = Human('인간49')
    hu50 = Human('인간50')
    hu51 = Human('인간51')
    hu52 = Human('인간52')
    hu53 = Human('인간53')
    hu54 = Human('인간54')
    hu55 = Human('인간55')
    hu56 = Human('인간56')
    hu57 = Human('인간57')
    hu58 = Human('인간58')
    hu59 = Human('인간59')
    hu60 = Human('인간60')

    import random

    def election(number):
        vote = [0,0,0,0,0,0]
        for i in range(1, number+1):
            data = random.randint(1, 5)
            vote[data]+=1
        maximum = 0
        number = 0
        for n in range(1, 6):
            if vote[n] > maximum:
                maximum = vote[n]
                number = n
        return number, maximum

    d = list(election(60))

    people = [man, swings, woman, MB, ahn]
    for i in people:
        if i.number == d[0]:
            president = i.name

    print('기호 {}번, {:.1f}%의 득표율로 당선!'.format(d[0], d[1]*100/60))
    print('현 대통령 : %s' % (president))
    print('\n\n살아있는 사람 : %d\n' % (Human.total_count))
# world1()

kim = ManOne('김철수')
shin = ManOne('신영희')

def world2(obj1, obj2):
    print('{}의 인생이야기'.format(obj1.name))
    obj1 + obj2
    obj1 - obj2
    obj1.__del__()
# world2(kim, shin)
