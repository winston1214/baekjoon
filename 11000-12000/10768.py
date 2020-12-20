# @Author YoungMinKim
# baekjoon

import sys
month = int(sys.stdin.readline())
day = int(sys.stdin.readline())
if month<2:
    print('Before')
else:
    if month==2 and day == 18:
        print('Special')
    elif month==2 and day<18:
        print('Before')
    else:
        print('After')