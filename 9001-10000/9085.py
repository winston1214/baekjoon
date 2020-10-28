# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    ls = list(map(int,sys.stdin.readline().split()))
    print(sum(ls))