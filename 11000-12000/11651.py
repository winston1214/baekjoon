# @Author YoungMinKim
# baekjoon
import sys
N = int(sys.stdin.readline())
tmp = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    tmp.append((y,x))
result = sorted(tmp)
for i,j in result:
    print(j,i)