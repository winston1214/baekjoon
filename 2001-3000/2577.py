# @Author YoungMinKim
# baekjoon
a=int(input())
b=int(input())
c=int(input())
result = a*b*c
ls = []
for i in range(len(str(result))):
    ls.append(int(str(result)[i]))
for j in range(10):
    print(ls.count(j))
