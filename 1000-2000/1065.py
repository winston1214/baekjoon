# @Author YoungMinKim
# baekjoon

N=int(input())
cnt=0
if N<100:
    cnt=N
else:
    cnt=99
    for i in range(100,N+1):
        ls = list(str(i))
        if int(ls[1]) - int(ls[0]) == int(ls[2]) - int(ls[1]):
            cnt+=1
        else:
            continue
print(cnt)