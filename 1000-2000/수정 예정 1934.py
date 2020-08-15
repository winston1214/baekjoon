N=int(input())
tmp=[]
for i in range(N):
    tmp.append(list(map(int,input().split())))
tmp[0].sort()
a=tmp[0][0]
b=tmp[0][1]
r=a
while True:
    if a<b:
        r+=a
        a=r
    elif a>b:
        r+=b
        b=r
    else:
        break
print(r)


