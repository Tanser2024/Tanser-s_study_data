
n=int(input())
king=list(map(int,input().split()))
peo=[]
for _ in range(n):
    peo.append(tuple(map(int,input().split())))
s=king[0]
pe=sorted([(x[0]*x[1],x[0]) for x in peo],key=lambda p:p[0])
min_max=-float("inf")

for i in range(n):
    s*=pe[i][1]
    min_max=max(min_max,s//pe[i][0])
print(min_max)