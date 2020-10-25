# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
[print(i,end=' ') for i in sorted(x)]