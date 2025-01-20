n=int(input())
data=[]
for _ in range(n):
    a,b=map(int,input().split())
    data.append((a,b))
data1=sorted(data,key=lambda x:x[0])
data.sort(key=lambda x:x[1])
if data1!=data:
    print("Happy Alex")
else:
    print("Poor Alex" )