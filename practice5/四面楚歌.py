n,m=map(int,input().split())
mat=[]
for _ in range(n):
    mat.append(list(map(str,input().split())))
s=[0]
for i in range(n):
    for j in range(m):
        a=int(mat[i][j])*int(mat[0][j]+mat[i][m-1]+mat[n-1][j]+mat[i][0])
        if a>s[0]:
            s[0]=a
print(s[0])