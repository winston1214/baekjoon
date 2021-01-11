# @Author YoungMinKim
# baekjoon

import sys
for _ in range(3):
    ls = list(map(int,sys.stdin.readline().split()))
    cnt = ls.count(1)
    if cnt == 4 :
        print('E')
    elif cnt == 3 :
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 1:
        print('C')
    else:
        print('D')