# @Author YoungMinKim
# baekjoon
N = int(input())
ls = []

for _ in range(N):
    ls.append(list(map(int,input().split()))[1:])
for i in ls:
    avg = sum(i)/len(i)
    cnt=0
    for j in i:
        if j > avg:
            cnt+=1
        else:
            continue
    print('%.3f%%'%((cnt/len(i))*100))