# @Author YoungMinKim
# baekjoon

import sys
x = int(sys.stdin.readline())
if x %2 ==0:
    n = x//2
    print(n**2+2*n+1)
else:
    n = x//2+1
    print(n**2+n)
