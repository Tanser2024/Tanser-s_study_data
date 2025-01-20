dirc=[(0,1),(0,-1),(-1,0),(1,0)]
def dfs(m,x,y,c,n,d):
    m[x][y]="#"
    for k in d:
        tx=x+k[0];ty=y+k[1]
        if 0<=tx<n and 0<=ty<n and m[tx][ty]==c:
            dfs(m,tx,ty,c,n,d)
k=int(input())
for _ in range(k):
    n=int(input())
    matrix=[]
    r=0;b=0
    for _ in range(n):
        dm=list(input())
        matrix.append(dm)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]=="r":
                dfs(matrix,i,j,"r",n,dirc)
                r+=1
            elif matrix[i][j]=="b":
                dfs(matrix,i,j,"b",n,dirc)
                b+=1
    print(r,b)