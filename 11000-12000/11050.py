# @Author YoungMinKim
# baekjoon
def factorial(N):
    if N == 1:
        return 1
    elif N == 0:
        return 1
    else:
        return N*factorial(N-1)
N,K = map(int,input().split())
print(int(factorial(N)/(factorial(N-K)*factorial(K))))