# @Author YoungMinKim
# baekjoon

import sys
dic = {}
for i in range(1,31):
    dic[i] = 1
for j in range(28):
    x = int(sys.stdin.readline())
    if x in dic:
        dic[x]=2
result = sorted(dic.items(),key=(lambda x: x[0]))
for i in result:
    if i[1] == 1:
        print(i[0])
