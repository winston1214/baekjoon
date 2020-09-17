# @Author YoungMinKim
# baekjoon
from collections import deque
import sys
que = deque([])
N = int(sys.stdin.readline())
for _ in range(N):
    x = sys.stdin.readline()[:-1]
    if x.split()[0] == 'push_back':
        que.append(x.split()[1])
    elif x.split()[0] == 'push_front':
        que.reverse()
        que.append(x.split()[1])
        que.reverse()
    elif x == 'pop_front':
        if len(que) != 0:
            print(que.popleft())
        else: print(-1)
    elif x == 'pop_back':
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)
    elif x == 'size':
        print(len(que))
    elif x == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif x == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif x == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
