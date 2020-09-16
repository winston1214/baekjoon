# @Author YoungMinKim
# baekjoon
import sys
while True :
    a,b = map(int,sys.stdin.readline().split())
    if a == b == 0:
        break
    if a>b and a%b == 0:
        print('multiple')
    elif a<b and b%a == 0:
        print('factor')
    else:
        print('neither')
