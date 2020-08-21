N=int(input())
nam = N%5
five_bongji = N//5
three_bongji = nam//3
if nam%3 != 0:
    print(-1)
else:
    print(five_bongji+three_bongji)