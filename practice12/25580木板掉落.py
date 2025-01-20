h,l,n=map(int,input().split())
import math
min_num=math.floor(n/2)+1

speed=sorted(list(map(int,input().split())))

H=h-5*(l/speed[min_num-1])**2
print("%.2f"%H)
