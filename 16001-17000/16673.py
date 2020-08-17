# @Author YoungMinKim
# baekjoon
c,k,p = map(int,input().split())
result=0
for i in range(1,c+1):
    result+=((k*i)+p*i**2)
print(result)