import sys
N,K = map(int,sys.stdin.readline().split())
idx = []
for i in range(1,N+1):
    if N%i == 0:
        idx.append(i)
if K<=len(idx):
    print(0)
else:    
    print(idx[K-1])
