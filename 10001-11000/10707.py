# @Author YoungMinKim
# baekjoon

import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
p = int(sys.stdin.readline())
X = a*p
if p<=c:
    Y = b
elif p>c:
    Y = b+(p-c)*d
print(min(X,Y))