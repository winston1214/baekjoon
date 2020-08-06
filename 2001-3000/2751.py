# @Author YoungMinKim
# baekjoon
# pypy3로 제출
n=int(input())
ls=[]
for i in range(n):
    ls.append(int(input()))    
ls.sort()
x=set(ls)
for i in x:
    print(i)