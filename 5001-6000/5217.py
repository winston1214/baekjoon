# @Author YoungMinKim
# baekjoon

import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    start = 1
    print("Pairs for {}:".format(n), end = ' ')
    for k in range((n-1)//2):
        if k != 0:
            print(',', end = ' ')
        print(start, n - start, end = '')
        start += 1
        
    print()