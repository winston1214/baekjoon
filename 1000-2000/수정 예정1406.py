import sys
from collections import deque
X = list(sys.stdin.readline()[:-1])
N = int(sys.stdin.readline())
cursor = len(X)
X = deque(X)
for _ in range(N):
    op = sys.stdin.readline()[:-1]
    if op.split()[0] == 'P':
        
        X.insert(cursor,op.split()[1])
        cursor+=1
    elif op == 'L':
        if cursor == 0:
            pass
        else:
            cursor-=1
    elif op == 'D':
        if cursor == len(X):
            pass
        else:
            cursor+=1
    elif op == 'B':
        if cursor == 0:
            pass
        else:
            X.remove(X[cursor-1])
            cursor-=1
for i in X:
    print(i,end='')