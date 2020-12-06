import sys
block = []
for _ in range(9):
    x = list(map(int,sys.stdin.readline().split()))
    block.append(x)
maximum = max(sum(block,[]))
print(maximum)
row = 1
breaker=False
for i in block:
    col = 1
    for j in i:
        if j == maximum:
            print(row,col)
            breaker=True
            break
        else:
            col+=1
    if breaker:
        break
    row+=1