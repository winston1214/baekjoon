# @Author YoungMinKim
# baekjoon

import sys
x = int(sys.stdin.readline())
cnt = 0
num = 666
while True:
    if '666' in str(num):
        cnt+=1
    if cnt == x:
        print(num)
        break
    num+=1
