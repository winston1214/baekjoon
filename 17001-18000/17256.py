# @Author YoungMinKim
# baekjoon
a_x,a_y,a_z = map(int,input().split())
c_x,c_y,c_z = map(int,input().split())
b_x= c_x - a_z
b_y= c_y/a_y 
b_z = c_z-a_x 
print(int(b_x),int(b_y),int(b_z))