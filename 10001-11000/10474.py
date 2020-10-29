# @Author YoungMinKim
# baekjoon
import sys
while True:
    a,b = map(int,sys.stdin.readline().split())
    if a==b==0:
        break
    num = a//b
    child = a%b
    print('{} {} / {}'.format(num,child,b))