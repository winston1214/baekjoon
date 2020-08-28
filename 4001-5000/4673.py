# @Author YoungMinKim
# baekjoon
def self_number():
    ls = []
    for i in range(1,10001):
        ls.append(i + sum([int(j) for j in str(i)]))

    return set(range(1,10001)) - set(ls)
result = sorted(self_number())
for i in result:
    print(i)