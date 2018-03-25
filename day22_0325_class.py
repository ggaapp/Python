""" 클래스 객체/오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
클래스변수 / 인스턴스변수는, 변수의 접근 권한(소유권)에 관한 문제
  - '클래스 객체'를 독립시키려면, 접근권한, 소유권, 상호관계를 명확히 해야 함

@staticmethod = 클래스 객체와 상관없지만 끼워넣은 매서드
@classmethod = 인스턴스로 접근해서 클래스변수를 변경시키는 매서드
"""
# import _script_run_utf8
# _script_run_utf8.main()

SEPERATOR = "--"*20 +"\n"


class Human(object):   # (T)his(I)s(H)uman = 파스칼타입
    total_count = 0    # 클래스 변수 = 전체적용
    icon = '무던함'     # icon (성격)

    def __init__(self, name):       # 매직매서드(생성자)
        Human.total_count += 1
        self.name = name

    def __add__(self, other_obj):
        print("'{}'와 '{}'는 결혼했습니다.".format(self.name, other_obj.name))

    def __sub__(self, other_obj):
        print("'{}'와 '{}'는 이혼했습니다.".format(self.name, other_obj.name))

    def __del__(self):
        print("'{}'는 죽었습니다.".format(self.name))

    def say_hello(self, other_obj):        # 기능을 함수(매서드)
        print("안녕하세요 '{}'님, 저는 '{}'입니다.".format(other_obj.name, self.name))

    def say_status(self):       #
        print("'{}' 님의 성격은 '{}' 입니다.".format(self.name, self.icon))


class ManOne(Human):

    def __init__(self, name):
        super().__init__(name)
        print("'{}'님이 입장하셨습니다. 총 생존자 {}명".format(self.name, super().total_count))

    """ 스태틱 메소드는 객체기능과 상관x 편의상 포함시켜야 할 때 """
    @staticmethod
    def show_shortened_life_story_with(obj1, obj2):
        print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
              '\n--------------------'.format(obj1.name, obj2.name))
        obj1 + obj2       # __add__() 매직매서드 실행
        obj1 - obj2       # __Sub__() 매직매서드 실행
        obj1.__del__()    # del().. __del__ 매직매서드 실행

    """ 클래스 메소드는 인스턴스 명의로 클래스에 접근할 방법을 열어준다 """
    @classmethod
    def show_count(cls):
        print('전체 인원은=', cls.total_count)

m0=ManOne('김철수')
m1=ManOne('신영희')

m0.show_shortened_life_story_with(m0, m1)
m0.show_count()

def test1_class_instance():
    ManOne.icon='허경영'
    m0.icon='난폭함'
    print("철수성격=", m0.icon)
    m1.icon='상냥함'
    print("영희성격=", m1.icon)

    ManOne.inner='좀비'
    print('ManOne Inner 형성 = ', ManOne.inner)
    print(m0.inner)
    print(m1.inner)
