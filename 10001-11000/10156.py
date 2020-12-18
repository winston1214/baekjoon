# @Author YoungMinKim
# baekjoon

import sys
K,N,M = map(int,sys.stdin.readline().split())
result = K*N-M
if result<=0 : print(0)
else:
    print(result)