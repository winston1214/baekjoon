# @Author YoungMinKim
# baekjoon

n = int(input())
num1=0
for i in range(n-1,-1,-1):
    print(' '*num1+'*'*(2*i+1))
    num1+=1
num2 = n-2
for j in range(1,n):
    print(' '*num2+'*'*(2*j+1))
    num2-=1