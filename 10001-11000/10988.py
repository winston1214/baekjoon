# @Author YoungMinKim
# baekjoon
import sys
x=list(sys.stdin.readline()[:-1])
y = x.copy()
y.reverse()
if x == y:
    print(1)
else:
    print(0)
