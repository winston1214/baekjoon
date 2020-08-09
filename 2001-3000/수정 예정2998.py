a=input() # 2진수
a=list(a)
hap = 0
for i in range(len(a)):
    hap+=int(a[i])*2**(len(a)-(i+1))
print(hap) # 십진수로 변환
