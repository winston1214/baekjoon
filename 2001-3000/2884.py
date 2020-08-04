# @Author YoungMinKim
# baekjoon

h,m = map(int,input().split())
if m<45:
    if h == 0:
        print(23,m+60-45)
    else:
        print(h-1,m+60-45)
else:
    print(h,m-45)