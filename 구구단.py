num=1

while (num != 0):
    print ('구구단 몇 단을 계산할까요? : ')
    num=int(input())
    if (num==0):
        break
    if (1<=num<=9):
        print ('구구단', num,'단을 계산합니다.')
        for i in range (1,10):
            print(num, 'x', i, '=', num*i)
    else:
        print ('잘못입력했습니다. 1~9 사이 숫자를 입력하세요.')

print('구구단을 종료합니다.')
        