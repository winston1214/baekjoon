# @Author YoungMinKim
# baekjoon
high_buger= int(input())
mid_buger=int(input())
low_buger = int(input())
coke = int(input())
soda = int(input())
buger=[high_buger,mid_buger,low_buger]
drink = [coke,soda]
buger.sort();drink.sort()
print(buger[0]+drink[0]-50)