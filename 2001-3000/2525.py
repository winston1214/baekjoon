# @Author YoungMinKim
# baekjoon
import datetime as dt
h,m = map(int,input().split())
m2 = int(input())
now = str(dt.timedelta(hours=h,minutes=m)+dt.timedelta(minutes = m2))
h=now.split(':')[0]
m=now.split(':')[1]
if len(h)>2:
    h = h.split(',')[1].split(' ')[1]
print(int(h),int(m))