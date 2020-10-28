# @Author YoungMinKim
# baekjoon

import sys
a = list(sys.stdin.readline()[:-1])
h = 10
for i in range(len(a)):
    if i == len(a)-1:
        break
    if a[i] == a[i+1]:
        h+=5
    else:
        h+=10
print(h)