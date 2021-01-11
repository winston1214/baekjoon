# @Author YoungMinKim
# baekjoon

import sys
a,b= map(str,sys.stdin.readline().split())
a_list, b_list,s = [0]*10,[0]*10,0
for i in a:
    a_list[ord(i)-48] +=1
for i in b:
    b_list[ord(i)-48] +=1
for i in range(1,10):
    for j in range(1,10):
        s += i*j*(a_list[i]*b_list[j])
print(s)