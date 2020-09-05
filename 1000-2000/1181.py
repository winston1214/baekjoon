# @Author YoungMinKim
# baekjoon
import sys
N = int(sys.stdin.readline())
dic = []
for _ in range(N):
    x = sys.stdin.readline().split()[0]
    dic.append((len(x),x))
sort_dic = sorted(set(dic))
for i in sort_dic:
    print(i[1])
