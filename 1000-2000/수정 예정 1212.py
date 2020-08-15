# 8진수를 입력받고 2진수를 출력하는 프로그램
N=list(input())
ten=0
for i in range(len(N)): # 10진수로 변환 후
    ten+=int(N[-(i+1)])*(8**i)
tmp=[]
while ten!=0:
    tmp.append(ten%2) # 2진수 list에 저장
    ten=ten//2 
result=''
for i in range(len(tmp)): # reverse 되어 있으므로 reverse시킴
    result+=str(tmp[-(i+1)])
print(int(result)) # 숫자형으로 출력