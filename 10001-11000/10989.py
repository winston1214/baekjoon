# @Author YoungMinKim
# baekjoon

import sys
N=int(sys.stdin.readline())

result = [0]*10001
for _ in range(N):
    a=int(sys.stdin.readline())
    result[a] = result[a]+1
for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)