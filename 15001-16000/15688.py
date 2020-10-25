# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
tmp = []
for i in range(N):
    tmp.append(int(sys.stdin.readline()))
[print(i) for i in sorted(tmp)]