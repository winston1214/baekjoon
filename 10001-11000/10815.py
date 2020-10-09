# @Author YoungMinKim
# baekjoon

import sys
a= int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().split()))
b = int(sys.stdin.readline())
Y = list(map(int,sys.stdin.readline().split()))
dic = {}
for i in X:
    dic[i] = True
for i in Y:
    if i in dic:
        print(1,end=' ')
    else:
        print(0,end=' ')
