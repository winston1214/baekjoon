# @Author YoungMinKim
# baekjoon
import datetime
h,m,s = map(int,input().split())
s2 = int(input())
now = str(datetime.timedelta(hours=h,minutes=m,seconds=s)+datetime.timedelta(seconds=s2))
h = now.split(':')[0]
m = now.split(':')[1]
s = now.split(':')[2]
if len(h)>2:
    h = h.split(',')[1].split(' ')[1]
print(int(h),int(m),int(s))