directions=[(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,1),(1,0),(1,-1)]
def dfs(mat,x,y):
    global now_num
    mat[x][y]="."
    for dx,dy in directions:
        tx=x+dx;ty=dy+y
        if mat[tx][ty]=="W":
            now_num+=1
            mat[x][y]="."
            dfs(mat,tx,ty)
t=int(input())
for _ in range(t):
    N,M=map(int,input().split())
    matrix=[["."]*(M+2)]
    for _ in range(N):
        matrix.append(["."]+list(input())+["."])
    matrix.append(["."]*(M+2))
    max_num=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if matrix[i][j]=="W":
                now_num=1
                dfs(matrix,i,j)
                max_num=max(max_num,now_num)
    print(max_num)