# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
x=0
for _ in range(9):
    x+= int(sys.stdin.readline())
print(N-x)