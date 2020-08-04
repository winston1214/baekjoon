# @Author YoungMinKim
# baekjoon

a=int(input())
b=int(input())
b=list(str(b))
result=0
num=0
for i in range(len(b)-1,-1,-1):
    print(a*int(b[i]))
    result += (10**(num))*(a*int(b[i]))
    num+=1
print(result)