from game_character import *

class Monster(Character):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Monster._total_count += 1


class FireMonster(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        FireMonster._total_count += 1
        print("['%-17s'] 생성되었습니다." % self.__class__.__name__)


class IceMonster(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        IceMonster._total_count += 1
        print("['%-17s'] 생성되었습니다." % self.__class__.__name__)

if __name__ == "__main__":
    a = Monster()
    b = Monster()

    print("캐릭터의 개수=", Character._total_count)
    print("몬스터의 개수=", Monster._total_count)
    print("불괴물의 개수=", FireMonster._total_count)
    print("얼음괴물의 개수=", IceMonster._total_count)
