# @Author YoungMinKim
# baekjoon

N,M  = map(int,input().split())
matrix1 = []
for _ in range(N):
    matrix1.append(list(map(int,input().split())))
M,K = map(int,input().split())
matrix2=[]
for _ in range(M):
    matrix2.append(list(map(int,input().split())))

result = [[0 for _ in range(K)] for _ in range(N)] 

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += matrix1[n][m] * matrix2[m][k]
for i in result:
    for j in i:
        print(j,end=' ')
    print()