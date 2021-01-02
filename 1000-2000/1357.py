# @Author YoungMinKim
# baekjoon

import sys
a,b = sys.stdin.readline().split()
a,b = list(a),list(b)
a.reverse()
b.reverse()
result = list(str(int(''.join(a)) + int(''.join(b))))
result.reverse()
print(int(''.join(result)))

