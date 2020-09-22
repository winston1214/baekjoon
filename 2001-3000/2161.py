# @Author YoungMinKim
# baekjoon
import sys
from collections import deque
N = int(sys.stdin.readline())
tmp = deque([i for i in range(1,N+1)])
result=[]
while True:
    result.append(tmp.popleft())
    if len(tmp) == 0:
        break
    x = tmp.popleft()
    tmp.append(x)
[print(i,end=' ') for i in result]