# @Author YoungMinKim
# baekjoon

import itertools
import sys
while True:
    a = list(map(int,sys.stdin.readline().split()))
    if a == [0]:
        break
    event = list(itertools.combinations(a[1:], 6))
    for i in event:
        for j in i:
            print(j,end=' ')
        print()
    print()