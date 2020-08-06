# @Author YoungMinKim
# baekjoon
N=int(input())
tmp=[]
for i in range(N):
    tmp.append(int(input()))
tmp.sort()
for i in tmp:
    print(i)