# @Author YoungMinKim
# baekjoon

import sys
idx = 1
while True:
    n0 = int(sys.stdin.readline())
    if n0 == 0:
        break
    n1 = 3*n0
    if n1 % 2 == 0:
        n2 = n1/2
    else:
        n2 = (n1+1)/2
    n3 = 3*n2
    n4 = n3//9
    if n1 % 2 == 0:
        result = 2 * n4
        print('{}. even {}'.format(idx,int(n4)))
    else:
        result = 2*n4+1
        print('{}. odd {}'.format(idx,int(n4)))
    idx+=1