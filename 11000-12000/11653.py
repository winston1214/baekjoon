# @Author YoungMinKim
# baekjoon
import sys
import math
N = int(sys.stdin.readline())
num = 2
result = []
while N != 1:
    if math.gcd(N,num) != 1:
        result.append(num)
        N = N // num
    else:
        num+=1
[print(x) for x in result]