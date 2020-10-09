# @Author YoungMinKim
# baekjoon

from collections import deque
import sys
N = int(sys.stdin.readline())
class queue:
    def __init__(self):
        self.ls = deque([])
    def push(self,num):
        self.ls.append(num)
    def pop(self):
        if self.size() == 0:
            return -1
        else:
            return self.ls.popleft()
    def size(self):
        return len(self.ls)
    def front(self):
        if self.size() == 0:
            return -1
        return self.ls[0]
    def back(self):
        if self.size() == 0:
            return -1
        return self.ls[-1]
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
q= queue()
for _ in range(N):
    x = sys.stdin.readline()[:-1]
    if x.split()[0] == 'push':
        q.push(int(x.split()[1]))
    elif x == 'pop':
        print(q.pop())
    elif x == 'front':
        print(q.front())
    elif x=='size':
        print(q.size())
    elif x == 'empty':
        print(q.empty())    
    elif x == 'back':
        print(q.back())
