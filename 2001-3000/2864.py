# @Author YoungMinKim
# baekjoon
a,b = input().split()
maximum = int(a.replace('5','6')) + int(b.replace('5','6'))
minimum = int(a.replace('6','5'))+ int(b.replace('6','5'))
print(minimum,maximum)