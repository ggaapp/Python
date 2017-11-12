SEPARATOR = '\n' + '__'*20 + '\n\n'

RUN_IMAGE = [
 '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..''',
 '''
 ..oo...
 oooo...
 ..oo...
 ..oo...
 oooooo.''',
 '''
 .ooooo.
 o...oo.
 ..ooo..
 ooo....
 oooooo.''',
 '''
 .ooooo.
 ....oo.
 .oooo..
 ...ooo.
 ooooo..''',
 '''
 ...oo..
 .oo.o..
 oo..o..
 oooooo.
 ....o..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 ....oo.
 ooooo..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 oo..oo.
 .oooo..''',
 '''
 oooooo.
 o...oo.
 ...oo..
 ..oo...
 .oo....''',
 '''
 .ooooo.
 oo..oo.
 .oooo..
 oo..oo.
 .oooo..''',
 '''
 .ooooo.
 oo...o.
 oooooo.
 ....oo.
 ooooo..''',
 ]

print(RUN_IMAGE[0], '\n\n\n\n\n\n\n\n')

import time
import os

for k in range(0, 10):
    RUN_IMAGE[k] = RUN_IMAGE[k].replace('.', '∵').replace('o', '■')

set_time = input('sec : ')


digit = len(set_time)
num = []
sec = int(set_time)
for m in range(1, digit + 1):
    rm = sec % 10
    num.append(rm)
    sec = int((sec - rm)/10)
    print(num[m-1])

num.reverse()
sec = int(set_time)

os.system("cls")
cnt = 0
for n in range(0, sec):
    print('\n\n\n\n\n\n\n')
    for i in range(0, digit):
        if i == digit-1:
            print(RUN_IMAGE[num[i]-cnt])
        else:
            print(RUN_IMAGE[num[i]])
    time.sleep(0.69)
    os.system("cls")
    cnt = cnt + 1
