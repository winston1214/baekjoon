# @Author YoungMinKim
# baekjoon
x=input()
string = []
for i in range(97,123):
    string.append(chr(i))
for j in range(len(x)):
    for i in range(len(string)):
        if x[j] == string[i]:
            string[i] = j
for v in range(len(string)):
    if type(string[v]) == str:
        string[v] = -1
for k in string:
    print(k,end=' ')