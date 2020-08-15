# @Author YoungMinKim
# baekjoon
N=int(input())
for i in range(N,0,-1):
    print('{}{}'.format(' '*(N-i),'*'*i))