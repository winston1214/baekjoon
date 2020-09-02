# @Author YoungMinKim
# baekjoon

import math
import sys
def isPrime(num):
    if num==1: return False
    n = int(math.sqrt(num))
    for i in range(2,n+1):
        if num % i ==0:
            return False
    return True
tmp = list(range(2,123456*2+1))
prime_ls = []
for i in tmp:
    if isPrime(i):
        prime_ls.append(i)
while True:
    cnt=0
    N = int(sys.stdin.readline())
    if N == 0: break
    for i in prime_ls:
        if i>N and i<=2*N:
            cnt+=1
    print(cnt)