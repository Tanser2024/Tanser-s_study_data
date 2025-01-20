n,m=map(int,input().split())
stu=sorted(list(map(int,input().split())))
D=sorted([stu[i]-stu[i-1] for i in range(1,n)])
s=sum(D)
for i in range(m-1):
    s-=D[n-2-i]
print(s)