import sys
import math
N = int(sys.stdin.readline())
for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    r1= x[2]
    r2 = x[-1]
    if r1<r2:
        r1,r2 = r2,r1
    d = math.sqrt(math.pow(x[0]-x[3],2)+math.pow(x[1]-x[4],2))
    if r1+r2 == d or r1-r2 == d:
        if d == 0 and r1 == r2:
            print(-1)
        else:
            print(1)
    elif r1-r2 < d and r1+r2>d:
        print(2)
    elif r1+r2<d or d<r1-r2:
        print(0)