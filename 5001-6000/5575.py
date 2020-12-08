# @Author YoungMinKim
# baekjoon

import sys
import datetime
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
c = list(map(int,sys.stdin.readline().split()))
def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds
for i in [a,b,c]:
    x = datetime.time(i[0],i[1],i[2])
    y = datetime.time(i[3],i[4],i[5])
    result = datetime.timedelta(hours=i[3],minutes = i[4],seconds = i[5])-datetime.timedelta(hours=i[0],minutes=i[1],seconds=i[2])
    hours, minutes, seconds = convert_timedelta(result)
    print(hours,minutes,seconds)