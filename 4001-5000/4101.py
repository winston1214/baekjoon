# @Author YoungMinKim
# baekjoon

import sys
while True:
    x,y = map(int,sys.stdin.readline().split())
    if x == y == 0:
        break
    if x>y:
        print('Yes')
    else:
        print('No')