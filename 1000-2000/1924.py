# @Author YoungMinKim
# baekjoon
import datetime
m,d = map(int,input().split())
now = datetime.datetime(2007,m,d)
dic={0:"MON",1:"TUE",2:"WED",3: "THU",4: "FRI",5: "SAT",6:"SUN"}
for i in dic.keys():
    if now.weekday() == i:
        print(dic[i])
    else:
        continue