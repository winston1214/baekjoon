# @Author YoungMinKim
# baekjoon

import sys
x = int(sys.stdin.readline())
if x%5 != 0:
    print(x//5 +1)
else:
    print(x//5)