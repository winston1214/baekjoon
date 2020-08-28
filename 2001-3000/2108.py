# @Author YoungMinKim
# baekjoon
import sys
from collections import Counter
N= int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
avg=sum(arr)/len(arr)
median = arr[len(arr)//2]
mode = Counter(arr).most_common() # count value
maximum = mode[0][1]
tmp=[]
for i in mode:
    if i[1] == maximum:
        tmp.append(i[0])
print(round(avg))
print(median)
if len(tmp)==1:
    print(sorted(tmp)[0])
else:
    print(sorted(tmp)[1]) 

print(max(arr) - min(arr))    

    
