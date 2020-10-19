# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
result = 0
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    result += y%x
print(result)