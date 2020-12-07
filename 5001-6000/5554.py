# @Author YoungMinKim
# baekjoon

import sys
a= int(sys.stdin.readline())
b= int(sys.stdin.readline())
c= int(sys.stdin.readline())
d= int(sys.stdin.readline())

all_sec = a+b+c+d

print(all_sec//60)
print(all_sec%60)
