""" CAR INFORM """

FORM_INTRO = '''\
=================================
\tVEHICLE INFORMATION
---------------------------------
1. MODEL      : %s (%s)
2. MAX SPEED  :      %d km/h
3. ACCELARATE :   +_ %d km/h
4. STATUS     :      %d km/h
---------------------------------\n\n\n'''


class Car(object):
    _total_count = 0
    _kind = ''
    _car_dict = dict()

    def __init__(self, arg_model):
        Car._total_count += 1
        Car._car_dict[Car._total_count] = [arg_model, self._kind]
        print("['%-8s']!! A NEW CAR!! has come ... total: (%s)" % (arg_model, Car._total_count))
        self.attr = {
            'model' : arg_model,
            'kind' : self._kind,
            'max_speed' : 140,
            's_able' : 2,
            'speed' : 0
        }

    def show_status(self):
        args = tuple(self.attr.values())
        for item in Car._car_dict:
            print('\n\n', item)
        print(FORM_INTRO % args)

    def set_speed_up(self):
        if self.attr['max_speed'] - self.attr['speed'] <self.attr['s_able']:
            self.attr['speed'] = self.attr['max_speed']
        if self.attr['speed'] + self.attr['s_able'] <= self.attr['max_speed']:
            self.attr['speed'] += self.attr['s_able']
        if self.attr['speed'] == self.attr['max_speed']:
            return True

    def set_speed_down(self):
        if self.attr['speed'] < self.attr['s_able']:
            self.attr['speed'] = 0
        if self.attr['speed'] - self.attr['s_able'] >= 0:
            self.attr['speed'] -= self.attr['s_able']
        if self.attr['speed'] == 0:
            return False

    def say_speed(self, bool):
        print('PRESENT SPEED = %d km/h' % (self.attr['speed']))
        if bool==True:
            print('== 최고속도(%d km/h)입니다. ==' % (self.attr['max_speed']))
        elif bool==False:
            print('---- 차가 정지 했습니다. ----')

class SportCar(Car):
    _total_count = 0
    _kind = '스포츠'

    def __init__(self, arg_model):
        super().__init__(arg_model)
        SportCar._total_count += 1
        self.attr = {
            'model':  arg_model,    # CAR NAME
            'kind':   self._kind,
            'max_speed':   300,     # MAXIMUM_SPEED
            's_able':   10,          # ACCELARATION
            'speed':   0,           # CURRENT SPEED
        }



class TruckCar(Car):
    _total_count = 0
    _kind = '화물용'

    def __init__(self, arg_model):
        super().__init__(arg_model)
        TruckCar._total_count += 1
        self.attr = {
            'model':  arg_model,    # CAR NAME
            'kind':   self._kind,
            'max_speed':   60,     # MAXIMUM_SPEED
            's_able':   1,          # ACCELARATION
            'speed':   0,           # CURRENT SPEED
        }

def speed_up_down(a):
    while a.attr['speed'] < a.attr['max_speed']:
        a.say_speed(a.set_speed_up())

    while a.attr['speed'] > 0:
        a.say_speed(a.set_speed_down())
