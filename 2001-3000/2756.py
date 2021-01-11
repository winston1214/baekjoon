# @Author YoungMinKim
# baekjoon

ls = []
for _ in range(7):
    x = int(input())
    if x % 2 != 0:
        ls.append(x)
if len(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(sorted(ls)[0])