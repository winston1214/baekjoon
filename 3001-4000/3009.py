# @Author YoungMinKim
# baekjoon

import sys
a_x,a_y = map(int,sys.stdin.readline().split())
b_x,b_y = map(int,sys.stdin.readline().split())
c_x,c_y = map(int,sys.stdin.readline().split())
x = [a_x,b_x,c_x]
y = [a_y,b_y,c_y]
for i in x:
    if x.count(i) == 1:
        print(i,end = ' ')
for j in y:
    if y.count(j) == 1:
        print(j)