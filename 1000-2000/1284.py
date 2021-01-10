# @Author YoungMinKim
# baekjoon

while True:
    num=input()
    if num=="0":
        break
    print((len(num)+1)+sum([2 if element=="1" else 4 if element=="0" else 3 for element in num]))