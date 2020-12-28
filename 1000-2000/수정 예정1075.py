import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
if a%b == 0:
    print('00')
else:
    mok = a//b
    if len(str(b*mok)) == len(str(a)):
        print(str(b*mok)[-2:])
    else:
        print(str(b*(mok+1))[-2:])
