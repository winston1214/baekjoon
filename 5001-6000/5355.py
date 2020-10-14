# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    x = list(sys.stdin.readline().split())
    try:
        if x[0].split('.'):
            num=float(x[0])
    except:
        num = int(x[0])
    for i in x[1:]:
        if i == '@':
            num*=3
        elif i == '%':
            num+=5
        else:
            num -= 7
    print('%.2f'%num)
