n=int(input())
a=reversed(list(map(int,input().split())))
dp=[]
import bisect
for i in range(n):
    temp=bisect.bisect_left(dp,a[i])
    if temp==len(dp):
        dp.append(temp)
