# @Author YoungMinKim
# baekjoon
a,b= map(int,input().split())
a=list(str(a))
b=list(str(b))
a.reverse()
b.reverse()
hap_a=''
hap_b=''
for i in range(3):
    hap_a+=a[i]
    hap_b+=b[i]
if int(hap_a)>int(hap_b):
    print(int(hap_a))
else:
    print(hap_b)
