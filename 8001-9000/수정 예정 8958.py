n=int(input())
ls=[]
for i in range(n):
    ls.append(input())
    score=0
    init_=0 # 초기화 변수
for j in range(len(ls)):
    if ls[j] == 'O':
        score+=1
        score+=init_
    elif ls[j] == 'X':
        score=0
        init_ = 0
print(score)
            