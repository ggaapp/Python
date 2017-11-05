"""
PYTHON CODING CONVENTION : 전통
-----
1.filename, variable = _ = temporary, __ = 내장함수, a, B(x), 1(x), !(x)
2. 1-line = 80 characters, (=recommendation)
3.Indent = 들여쓰기 (4칸 = space), Atom TAB = 4 spaces
     절대 혼용해서 쓰지 말 것
"""
# is comment

a = 300
b = 333

c = a * b

print(c, "\n")

""" INDENTATIONS """

""" (1) ---- for 루프"""
for n in range(5): # 0, 1, 2, 3, 4 .... n=4
    print('Hello Python')
print('END\n')

""" (2) ---- if문 """
if n>= 5:
    print('greater than 5...')
else:
    print('less than 5...')
    print('*****\n')
print('END\n')

print('n=', n)


""" (3) ---- 함수 : def (definition : 정의)
  Def(정의) - Call(호출-실행)
"""
# Function, 함수 정의
def a_add_b(a, b):      # a + b function / IN= a, b / OUT= c= a+b
    c = a + b
    return c
# Method, 메소드
def _a_add_b(a, b):      # a + b function / IN= a, b / OUT= c= a+b
    c = a + b
    print(c)


_a_add_b         # 함수 본체 (OBJECT)
print(_a_add_b)

_a_add_b(3, 4)

answer = a_add_b(3, 4) # 변수 할당, 지정= Assign
print(answer)

print(_a_add_b)
print(a_add_b)
print('STAR'.center(31))
print('BUCKS'.center(31))
for m in range(1, 7):
    print(" "*(15-m), '*'*(2*m-1))
for k in range(3):
    print("|".center(31))
print('M'*31)
