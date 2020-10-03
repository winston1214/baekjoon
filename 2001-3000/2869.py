# @Author YoungMinKim
# baekjoon
import sys
A,B,V = map(int,sys.stdin.readline().split())
if (V-A) % (A-B) == 0:
    result = (V-A) / (A-B) + 1
else:
    result = (V-A) / (A-B) + 2
print(int(result))
