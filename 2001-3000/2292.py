# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
a = 1
d = 6
room = 1
if N == 1:
    print(1)
else:
    while True:
        a = a+d
        room+= 1
        if N <= a:
            print(room)
            break
        d += 6