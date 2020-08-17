# @Author YoungMinKim
# baekjoon
def hanoi_tower(n,fr,tmp,to):
    if n == 1:
        print(fr,to)
    else:
        hanoi_tower(n-1,fr,to,tmp)
        print(fr,to)
        hanoi_tower(n-1,tmp,fr,to)
N=int(input())
print((2**N)-1)
hanoi_tower(N,1,2,3)