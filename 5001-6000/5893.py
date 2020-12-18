# @Author YoungMinKim
# baekjoon

import sys
x = sys.stdin.readline()
binary = '0b'+x
ten = int(binary,2) * 17
print(bin(ten)[2:])