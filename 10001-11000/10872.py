# @Author YoungMinKim
# baekjoon
def factorial(N):
    if N==1 or N==0:
        return 1
    else:
        return N*factorial(N-1)
N=int(input())
print(factorial(N))