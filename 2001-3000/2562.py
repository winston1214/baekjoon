# @Author YoungMinKim
# baekjoon
ls=[]
for _ in range(9):
    x=int(input())
    ls.append(x)
high = max(ls)
for i in range(len(ls)):
    if ls[i] == high:
        print(high)
        print(i+1)
    else:
        continue