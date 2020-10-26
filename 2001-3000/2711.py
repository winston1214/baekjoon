# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    num , string = sys.stdin.readline().split()
    ls = list(string)
    ls = ls[:int(num)-1] + ls[int(num):]
    print(''.join(ls))
    