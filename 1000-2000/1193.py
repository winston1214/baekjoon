# @Author YoungMinKim
# baekjoon

import sys
X = int(sys.stdin.readline())
hap = 1
n=2
while True:
    if X>hap and hap+n>X:
        if n%2 != 0:
            mom = X-hap
            child = hap+n -X+1
        else:
            mom = hap+n -X+1
            child = X-hap
        print('{}/{}'.format(child,mom))
        break
    elif X == hap:
        print('{}/{}'.format(n-1,1))
        break
    else:
        hap+=n
        n+=1