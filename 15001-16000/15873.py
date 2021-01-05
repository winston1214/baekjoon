# @Author YoungMinKim
# baekjoon

x = input()
if len(x) == 2:
    print(int(x[0]) + int(x[1]))
elif len(x) == 3:
    if x[:2] == '10':
        print(int(x[:2]) + int(x[-1]))
    else:
        print(int(x[0]) + int(x[1:]))
else:
    print(20)