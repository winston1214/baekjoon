# @Author YoungMinKim
# baekjoon
N=int(input())
tmp=[]
for i in range(N):
    tmp.append(input())
for i in range(N):
    x=tmp[i]
    repeat = int(x[0])
    for j in x[2:]:
        print(j*repeat,end='')
    print()