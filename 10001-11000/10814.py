# @Author YoungMinKim
# baekjoon
import sys
N = int(sys.stdin.readline())
ls = []
for i in range(N):
    x,y = sys.stdin.readline().split()
    ls.append((int(x),i,y))
for a,b,c in sorted(ls):
    print(a,c)