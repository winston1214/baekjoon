# @Author YoungMinKim
# baekjoon

import sys
import math
def combinations_len(p,r):
    return math.factorial(p)/(math.factorial(r)*math.factorial(p-r))

for _ in range(int(sys.stdin.readline())):
    N,M = map(int,sys.stdin.readline().split())
    if N<M:
        N,M = M,N
    print(int(combinations_len(N,M)))
    