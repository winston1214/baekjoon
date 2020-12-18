# @Author YoungMinKim
# baekjoon

import sys
L = int(sys.stdin.readline())
A = int(sys.stdin.readline()) # 국어 총 페이지
B = int(sys.stdin.readline()) # 수학 총 페이지
C = int(sys.stdin.readline()) # 국어 최대 페이지
D = int(sys.stdin.readline()) # 수학 최대 페이지
if A%C != 0:
    korean = A//C+1
else:
    korean = A//C
if B%D != 0:
    math = B//D+1
else:
    math = B//D
print(L-max([korean,math]))