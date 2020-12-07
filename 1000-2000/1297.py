# @Author YoungMinKim
# baekjoon

import sys
import math
a,b,c = map(int,sys.stdin.readline().split())
x = math.pow(b,2)+math.pow(c,2)
y = math.pow(a,2)/x
print(int(math.sqrt(y)*b),int(math.sqrt(y)*c))