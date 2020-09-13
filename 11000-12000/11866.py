# @Author YoungMinKim
# baekjoon
from collections import deque
import sys
a,b = map(int,sys.stdin.readline().split())
q = deque([i for i in range(1,a+1)])
result = []
while len(q) != 0:
    q.rotate(-b+1)
    result.append(q.popleft())
x= ', '.join(map(str,result))
print('<'+x+'>')
