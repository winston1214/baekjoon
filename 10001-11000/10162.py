# @Author YoungMinKim
# baekjoon

import sys
x= int(sys.stdin.readline())
A,B,C = 300,60,10
if x % 10 !=0:print(-1)
else:
    a = x//A
    b = (x - a*A)//B
    c = (x-a*A-b*B)//C
    print(a,b,c)