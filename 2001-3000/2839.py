# @Author YoungMinKim
# baekjoon
N=int(input())
five = []
three = []
nam5 = N//5
nam3 = N//3
result=[]
for i in range(nam5+1):
    five.append(5*i)
for j in range(nam3+1):
    three.append(3*j)
for i in five:
    for j in three:
        if i+j == N:
            result.append((i//5)+(j//3))
if len(result) == 0:
    print(-1)
else:
    print(min(result))
