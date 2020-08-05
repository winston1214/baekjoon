# @Author YoungMinKim
# baekjoon
string = input()
ls= list(string)
ls = [ls[i].lower() for i in range(len(ls))]
maximum=0
cnt=[]
final=''
for i in set(ls):
    cnt.append(ls.count(i))
    if maximum < ls.count(i):
        maximum = ls.count(i)
        final = i
    else:
        continue
if cnt.count(maximum)>1:
    print('?')
else:
    print(final.upper())