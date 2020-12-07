# @Author YoungMinKim
# baekjoon

import sys
x = list(map(int,sys.stdin.readline().split()))
for i,j in zip(x,[1,1,2,2,2,8]):
    print(j-i,end=' ')