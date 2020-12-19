# @Author YoungMinKim
# baekjoon

import sys
ls = []
for _ in range(6):
    ls.append(int(sys.stdin.readline()))
science = ls[:4]
science.remove(min(science))
science.append(max(ls[4:]))
print(sum(science))