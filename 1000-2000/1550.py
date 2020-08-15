# @Author YoungMinKim
# baekjoon
N=list(input())
dic = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
idx=0
result=0
for i in N:
    if i in dic.keys():
        result+=dic[i]*(16**(len(N)-1-idx))
        
    else:
        result+=int(i)*(16**(len(N)-1-idx))
        
    idx+=1
print(result)
