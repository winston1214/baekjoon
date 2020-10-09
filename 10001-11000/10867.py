# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))
unique = list(set(X))
for i in sorted(unique):
    print(i,end=' ')
