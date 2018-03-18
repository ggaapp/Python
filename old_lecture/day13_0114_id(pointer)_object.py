def test1_minimum_wage():
    while True:
        time = int(input('Enter working time : '))
        minimum_wage = int(input('Enter minimum wage : '))
        money = 12*minimum_wage+(time-12)*1.3*minimum_wage if time>12 else time*minimum_wage
        print('\nTotal pay is %d won' % (money))
        ck = input('\n\nContinue?(y/n) ')
        if ck=='y': print('='*30)
        elif ck=='n' : break
        else : exit(0)
# test1_minimum_wage()

def test2_factor():
    while True:
        num = int(input('Enter a number : '))
        print('-'*20)
        cnt=0
        for n in range(1, num+1):
            if num % n ==0:
                print(n)
                cnt+=1
        print('\n\nNumber of factor of %d : %d' % (num, cnt))
        ck = input('\n\nContinue?(y/n) ')
        if ck=='y': print('='*30)
        elif ck=='n' : break
        else : exit(0)
# test2_factor()

def test3_max_num():
    while True :
        max_num = 0
        for n in range(5):
            num = int(input('Enter a integer : '))
            max_num = num if num>max_num else max_num
        print('\nMaximum Value : %d' % (max_num))
        ck = input('\n\nContinue?(y/n) ')
        if ck=='y': print('='*30)
        elif ck=='n' : break
        else : exit(0)
# test3_max_num()

def test4_bubble_sort():
    while True :
        sort_list = list(input('Enter a array of 5 numbers : '))
        sorted_list = sort_list
        temp=sort_list[0]
        for k in range(4, -1, -1):
            for n in range(5):
                for i in range(5) :
                    if sort_list[n] == sorted_list[i]:
                        isin = 1
                        break
                if isin==1: temp=temp
                else : temp = sort_list[n] if sort_list[n]>=temp else temp
            isin=0
            sorted_list[k] = temp
        print(sorted_list)
        ck = input('\n\nContinue?(y/n) ')
        if ck=='y': print('='*40)
        elif ck=='n' : break
        else : exit(0)
test4_bubble_sort()
