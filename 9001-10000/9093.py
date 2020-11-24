# @Author YoungMinKim
# baekjoon

import sys
from collections import deque
N = int(sys.stdin.readline())
for _ in range(N):
    x = list(sys.stdin.readline().split())
    for i in x:
        print(i[::-1],end=' ')