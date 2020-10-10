# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
dic ={}
for i in a:
    try:dic[i] += 1
    except:dic[i]=1
for i in b:
    if i in dic:
        print(dic[i],end= ' ')
    else:
        print(0,end=' ')
