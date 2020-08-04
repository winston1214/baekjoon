# @Author YoungMinKim
# baekjoon
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
hap = 0
for i in (a,b,c,d,e):
    if i<40:
        i=40
    hap+=i
print(int(hap/5))