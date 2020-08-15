# @Author YoungMinKim
# baekjoon
N=int(input())
vote = []
for _ in range(N):
    x=int(input())
    vote.append(x)
if vote.count(0)>vote.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")