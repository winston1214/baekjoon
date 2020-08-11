# @Author YoungMinKim
# baekjoon
a=input() # 2진수
a=list(a)
hap = 0
for i in range(len(a)):
    hap+=int(a[i])*2**(len(a)-(i+1)) #10진수

result=[]
while True:
    mok = hap//8
    nam = hap%8
    result.append(nam)
    if mok>=8:
        hap=mok
        continue
    else:
        result.append(mok)
        break
result.reverse()
print(int("".join(map(str, result))))