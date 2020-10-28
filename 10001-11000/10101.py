# @Author YoungMinKim
# baekjoon
import sys
angle = []
for _ in range(3):
    angle.append(int(sys.stdin.readline()))
if sum(angle) != 180 : print('Error')
else:
    if angle.count(60) == 3 :print('Equilateral')
    else:
        for i in angle:
            if angle.count(i) ==2:
                print('Isosceles')
                break
        else:
            print('Scalene')
