# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
tmp=[]
for _ in range(N):
    tmp.append(int(sys.stdin.readline()))
for i in sorted(tmp,reverse=True):
    print(i)