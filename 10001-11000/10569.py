# @Author YoungMinKim
# baekjoon

N=int(input())
for _ in range(N):
    V,E = map(int,input().split())
    print(2-V+E)