# @Author YoungMinKim
# baekjoon

def one_to_two(num):
    if int(num)<10:
        return '0'+num
    else:return num
x= str(input())
cnt=0
n=one_to_two(x)
while True:
    hap = int(n[0])+int(n[1])
    hap=str(hap)
    cnt+=1
    hap = one_to_two(hap)
    if int(n[1]+hap[1]) == int(x):
        break
    else:
        n=n[1]+hap[1]
print(cnt)