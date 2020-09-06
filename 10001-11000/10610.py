# @Author YoungMinKim
# baekjoon

import sys
N = list(sys.stdin.readline()[:-1])
ls = sorted(N,reverse=True)
if ls[-1] != '0':
    print(-1)
elif int(''.join(ls)) % 30 ==0:
    print(int(''.join(ls)))
else:
    print(-1)

