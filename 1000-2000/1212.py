# @Author YoungMinKim
# baekjoon

# N=list(input())
# ten=0
# tmp=[]
# for i in range(len(N)):
#     ten+=int(N[-(i+1)])*(8**i)
# while ten!=0:
#     tmp.append(ten%2) 
#     ten=ten//2 
# result=''
# for i in range(len(tmp)): 
#     result+=str(tmp[-(i+1)])
# print(int(result))
print(bin(int(input(), 8))[2:])

