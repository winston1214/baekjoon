import sys
a,b = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))
y = list(map(int,sys.stdin.readline().split()))
for i in sorted(x+y):
    print(i,end=' ')