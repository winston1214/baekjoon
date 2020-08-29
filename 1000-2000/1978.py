import math
def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2,n+1):
        if num%i==0:
            return False
    return True
N=int(input())
x=list(map(int,input().split()))
cnt=0
for i in x:
    if isPrime(i):
        cnt+=1
print(cnt)