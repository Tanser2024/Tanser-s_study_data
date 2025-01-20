n,m1,m2=map(int,input().split())
from collections import defaultdict
mat1=defaultdict(int)
for _ in range(m1):
    x,y,z=map(int,input().split())
    mat1[(x,y)]=z
mat2=defaultdict(int)
for _ in range(m2):
    x,y,z=map(int,input().split())
    mat2[(x,y)]=z
outputs=[]
for i in range(n):
    for j in range(n):
        temp=0
        for k in range(n):
            if (i,k) in mat1 and (k,j) in mat2:
                temp+=mat1[i,k]*mat2[k,j]
        if temp:
            outputs.append((i,j,temp))
for x,y,z in outputs:
    print(x,y,z)
