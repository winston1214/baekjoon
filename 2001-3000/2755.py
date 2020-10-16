# @Author YoungMinKim
# baekjoon

import sys
N = int(sys.stdin.readline())
dic = {'A+':4.3,'A0':4.0,'A-':3.7,'B+':3.3,'B0':3.0,'B-':2.7,'C+':2.3,'C0':2.0,'C-':1.7,'D+':1.3,'D0': 1.0, 'D-': 0.7,'F':0.0}
hap=0
final = 0
for i in range(N):
    line = list(sys.stdin.readline().split())
    num = line[1]
    grade = dic[line[2]]
    hap += (int(num) * grade)
    final += int(num)
print('{:.02f}'.format(round(hap/final+(0.001 if hap/final*100 % 10 >= 5 else 0.000),2)))