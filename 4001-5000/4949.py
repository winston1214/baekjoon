# @Author YoungMinKim
# baekjoon

class Stack:
    def __init__(self):
        self.top=[]
    def isEmpty(self):return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top=[]
    def push(self,item): 
        self.top.append(item)
    def pop(self): 
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self): 
        if not self.isEmpty():
            return self.top[-1]
def checkBrackets(statement): # 괄호 검사기
    stack = Stack()
    for ch in statement:
        if ch in ('(','{','['): # 처음 시작 괄호를 스택에 넣는다.
            stack.push(ch)
        elif ch in (')',']','}'):
            if stack.isEmpty(): # 처음 시작 괄호가 스택에 없는데 닫는게 나와버리면 안됨.
                return False
            else:
                left = stack.pop() # 하나씩 뺀다.
                if (ch == ')' and left != '(') or (ch == '}' and left != '{') or (ch == ']' and left != '['):
                    return False # 닫는 괄호인데 하나씩 뺐을 때 짝이 안맞으면 안됨.
    return stack.isEmpty() # 비어야된다. 남아있으면 False 반환
import sys
while True:
    x = input()
    if x == '.':
        break
    if checkBrackets(x):
        print('yes')
    else:
        print('no')
