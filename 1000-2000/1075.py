# @Author YoungMinKim
# baekjoon

N, F = list(input()), int(input())
N[-2:] = ['0']*2
N = int(''.join(N))
while N % F != 0:
    N += 1
    
print(str(N)[-2:])