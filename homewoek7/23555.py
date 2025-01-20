n,m1,m2=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(m1)]
a=[[x[0],x[1]] for x in A]
B=[list(map(int,input().split())) for _ in range(m2)]
b=[[x[0],x[1]] for x in B]
c=[]
AB=[]
for i in range(n):
    C=[]
    for j in range(n):
        c=0
        for k in range(n):
            if [i,k] in a and [k,j] in b:
                c+=A[a.index([i,k])][2]*B[b.index([k,j])][2]
        C.append([i,j,c])
    AB.append(C)
for x in AB:
    for y in x:
        if y[2]!=0:
            print(" ".join(map(str,y)))