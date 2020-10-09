import sys
a = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
b = int(sys.stdin.readline())
y = list(map(int,sys.stdin.readline().split()))
dic={}
for i in x:
    dic[i]=True
for j in y:
    if j in dic:
        print(1)
    else:
        print(0)