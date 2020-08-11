# @Author YoungMinKim
# baekjoon
N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
b.reverse()
result=0
for i in range(N):
    result+= a[i]*b[i]
print(result)