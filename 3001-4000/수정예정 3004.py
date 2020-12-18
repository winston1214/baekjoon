import sys
x = int(sys.stdin.readline())
if x == 1:
    print(2)
even = 2
odd = 3
y=x
while y//2 != 0:
    if y % 2 == 0:
        even+=1
    else:
        odd+=1
    y = y/2
if x%2==0:
    print(even*even)
else:
    print(odd*(odd-1))
