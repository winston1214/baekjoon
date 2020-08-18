# @Author YoungMinKim
# baekjoon
N=int(input())
ls=[]
for i in range(N):
    ls.append(int(input()))
dasom = ls[0]
rev = ls[1:N]
if N == 1:
    print(0)
else:
    num=0
    rev= sorted(rev,reverse=True)
    while rev[0]>=dasom:
        dasom+=1
        rev[0]-=1
        num+=1
        rev = sorted(rev,reverse=True)
    print(num)