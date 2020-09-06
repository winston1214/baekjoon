# @Author YoungMinKim
# baekjoon
import sys
N = int(sys.stdin.readline())
x = list(sys.stdin.readline().split())
tmp = list(map(int,x))
tmp = sorted(tmp)
hap = 0
result = []
for i in tmp:
    hap+=i
    result.append(hap)
print(sum(result))