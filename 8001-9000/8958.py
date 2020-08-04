# @Author YoungMinKim
# baekjoon
n = int(input())
for i in range(n):
    Num = input()
    score = 0
    cnt = 0
    for j in range(len(Num)):
        if Num[j] == 'O':
            cnt += 1
            score += cnt
        elif Num[j] == 'X':
            score += 0
            cnt = 0
    print(score)