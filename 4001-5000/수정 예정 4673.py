num=[]
tmp=[]
# for i in range(1,10001):
#     num.append(i)
for i in range(1,101):
    if i<100:
        if i<10:
            i = '0'+str(i)
        i=str(i)
        tmp.append(int(i)+int(i[0])+int(i[1]))


