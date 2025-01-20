A_1,A_2=map(int,input().split())
A=[]
for i in range(A_1):
    a_1=list(map(int,input().split()))
    A.append(a_1)
B_1,B_2=map(int,input().split())
B=[]
for i in range(B_1):
    b_1=list(map(int,input().split()))
    B.append(b_1)
C_1,C_2=map(int,input().split())
C=[]
for i in range(C_1):
    c_1=list(map(int,input().split()))
    C.append(c_1)
D=[]
if A_2==B_1 and A_1==C_1 and B_2==C_2:
    for i in range(A_1):
        D_1=[]
        for j in range(B_2):
            d=0
            for k in range(A_2):
                d = d + A[i][k] * B[k][j]

            d=d+C[i][j]
            D_1.append(str(d))
        D.append(D_1)
    for line in D:
        print(" ".join(line))
else:
    print("Error!")




