# @Author YoungMinKim
# baekjoon
M=int(input())
N=int(input())
tmp=[]
for i in range(M,N+1):
    if str(i**(1/2))[-1] == '0' :
        tmp.append(i)
    else:
        continue
if len(tmp) == 0:
    print(-1)
else:
    print(sum(tmp))
    print(min(tmp))




