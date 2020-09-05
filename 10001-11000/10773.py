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
    def hap(self):
        return sum(self.tmp)
import sys
N = int(sys.stdin.readline())
s = stack()
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        s.push(x)
    else:
        s.pop()
print(s.hap())