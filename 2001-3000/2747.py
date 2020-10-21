# @Author YoungMinKim
# baekjoon

import sys
def fibonacci2(x):
    fib =[0,1]
    [fib.append(fib[-1]+fib[-2]) for i in range(x-1)]
    return fib
x = int(sys.stdin.readline())
print(fibonacci2(x)[-1])