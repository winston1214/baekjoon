# @Author YoungMinKim
# baekjoon

import sys
s,t,d = map(int,sys.stdin.readline().split())

time = d/(s*2)
print(int(time*t))