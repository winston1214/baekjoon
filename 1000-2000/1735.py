# @Author YoungMinKim
# baekjoon

import sys
from math import gcd
A1,A2 = map(int,sys.stdin.readline().split())
B1,B2 = map(int,sys.stdin.readline().split())
mom = A2*B2
child = B2*A1 + A2*B1
if gcd(mom,child) != 1:
    mom2 = mom // gcd(mom,child)
    child2 = child//gcd(mom,child)
    print(child2,mom2)
else:print(child,mom)