# @Author YoungMinKim
# baekjoon
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline())
    dic = {}
    for _ in range(a):
        x=list(sys.stdin.readline().split())
        price = int(x[0])
        name = x[1]
        dic[price] = name
    print(max(dic.items())[1])

