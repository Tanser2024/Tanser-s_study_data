def bfs(m,x,y,n):
    m[x][y]="1"
    for dx,dy in [(1,0),(0,1)]:
        if x+dx<n and y+dy<n and m[x+dx][y+dy]=="0":
            bfs(m,x+dx,y+dy,n)
N=int(input())
matrix=[]
for _ in range(N):
    m0=list(input().split())
    matrix.append(m0)
bfs(matrix,0,0,N)
if matrix[N-1][N-1]=="1":
    print("Yes")
else:
    print("No")