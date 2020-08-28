def self_number():
    li = []
    for i in range(1,10001):
        li.append(i + sum([int(j) for j in str(i)]))

    return set(range(1,10001)) - set(li)
print(sorted(self_number()))