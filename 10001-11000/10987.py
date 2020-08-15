# @Author YoungMinKim
# baekjoon
x=list(input())
mo = ['a','e','i','o','u']
result=0
for i in mo:
    result+=x.count(i)
print(result)