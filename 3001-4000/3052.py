# @Author YoungMinKim
# baekjoon
ls=[]
for _ in range(10):
    ls.append(int(input()))
result=[]
for i in ls:
    result.append(i%42)
print(len(set(result)))