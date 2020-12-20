# @Author YoungMinKim
# baekjoon

import sys
N,M,K = map(int,sys.stdin.readline().split())
print(min(M,K)+min(N-M,N-K))
