# @Author YoungMinKim
# baekjoon
import sys
N,K = sys.stdin.readline().split()
ls = list(sys.stdin.readline().split())
result = list(map(int,ls))
result = sorted(result)
print(result[int(K)-1])