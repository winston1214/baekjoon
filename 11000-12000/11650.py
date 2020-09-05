# @Author YoungMinKim
# baekjoon
import sys
N = int(sys.stdin.readline())
tmp = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    tmp.append((x,y))
result = sorted(tmp)
for i,j in result:
    print(i,j)