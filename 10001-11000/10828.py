# @Author YoungMinKim
# baekjoon

class stack:
    def __init__(self):
        self.tmp = []
    def push(self,x):
        self.tmp.append(x)
    def pop(self):
        if self.size() == 0:
            return -1
        else:
            return self.tmp.pop(-1)
    def size(self):
        return len(self.tmp)
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def top(self):
        if self.size()==0:
            return -1
        else:
            return self.tmp[-1]
import sys
s = stack()
N = int(sys.stdin.readline())
for _ in range(N):
    x = list(sys.stdin.readline().split())
    if x[0] == 'push':
        s.push(int(x[1]))
    elif x[0] == 'pop':
        print(s.pop())
    elif x[0]=='top':
        print(s.top())
    elif x[0] == 'size':
        print(s.size())
    else:
        print(s.empty())