# @Author YoungMinKim
# baekjoon

import sys
a = sys.stdin.readline()[:-1]
b = sys.stdin.readline()[:-1]
a10 = int('0b'+a,2)
b10 = int('0b'+b,2)
print(bin(a10*b10)[2:])