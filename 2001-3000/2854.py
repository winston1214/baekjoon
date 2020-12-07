# @Author YoungMinKim
# baekjoon

import sys
N,M = map(int,sys.stdin.readline().split())
a,b,c,d,e = map(int,sys.stdin.readline().split())

real_num = N*M
for i in (a,b,c,d,e):
    print(i-real_num,end=' ')