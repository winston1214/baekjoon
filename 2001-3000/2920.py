# @Author YoungMinKim
# baekjoon

a= list(map(int,input().split()))
ascending = sorted(a)
descending = sorted(a,reverse=True)
if a== ascending:
    print('ascending')
elif a == descending:
    print('descending')
else:
    print('mixed')
