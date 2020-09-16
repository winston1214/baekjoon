# @Author YoungMinKim
# baekjoon
from math import gcd
import sys
N = int(sys.stdin.readline())
f = list(sys.stdin.readline().split())
ls = sorted(list(map(int,f)))
print(ls[0]*ls[-1])