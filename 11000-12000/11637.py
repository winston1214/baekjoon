import sys
for _ in range(int(sys.stdin.readline())):
    ls=[]
    for j in range(int(sys.stdin.readline())):
        x=int(sys.stdin.readline())
        ls.append(x)
    if ls.count(sum(ls)/len(ls)) == len(ls):
        print('no winner')
    else:
        if sum(ls)/len(ls) < max(ls):
            print('')