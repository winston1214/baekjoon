# @Author YoungMinKim
# baekjoon
import sys
x,y,w,h = map(int,sys.stdin.readline().split())
result = [abs(x-w),abs(y-h),abs(x),abs(y)] # 점과 직선 사이 거리
print(min(result))