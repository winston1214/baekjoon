# @Author YoungMinKim
# baekjoon
x= list(map(int,input().split()))
if len(set(x)) == 1:
    print(10000+x[0]*1000)
elif len(set(x)) == 2:
    if x.count(x[0]) == 2:
        print(1000+x[0]*100)
    elif x.count(x[1]) == 2:
        print(1000 + x[1]*100)
else:
    print(max(x)*100)