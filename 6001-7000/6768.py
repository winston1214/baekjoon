# @Author YoungMinKim
# baekjoon

import itertools
import sys
x = int(sys.stdin.readline())
arr = [None]*(x-1)
result = list(itertools.combinations(arr,3))
print(len(result))