# @Author YoungMinKim
# baekjoon
import math
def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2,n+1):
        if num%i==0:
            return False
    return True
M = int(input())
N = int(input())
ls=[]
for i in range(M,N+1):
    if isPrime(i):
        ls.append(i)
if len(ls) == 0:
    print(-1)
else:    
    print(sum(ls))
    print(min(ls))