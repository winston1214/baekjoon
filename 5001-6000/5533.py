# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
score = []
for _ in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    score.append(x)
ls1 = []
ls2 = []
ls3 = []
for i in range(len(score)):
    ls1.append(score[i][0])
    ls2.append(score[i][1])
    ls3.append(score[i][2])
for idx,i in enumerate(ls1):
    if ls1.count(i)>=2:
        score[idx][0] = 0
for idx,i in enumerate(ls2):
    if ls2.count(i)>=2:
        score[idx][1] = 0
for idx,i in enumerate(ls3):
    if ls3.count(i)>=2:
        score[idx][2] = 0
for i in score:
    print(sum(i))