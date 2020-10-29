# @Author YoungMinKim
# baekjoon
import sys
def factorial(n):
    if(n > 1): 
        return n * factorial(n - 1)
    else: return 1
x = str(factorial(int(sys.stdin.readline())))
string = len(x)
num = int(''.join(reversed(x)))
long = len(str(num))
print(string - long)
