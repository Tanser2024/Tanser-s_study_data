n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
max_sum=-float("inf")
max_path=[(0,0)]
v={(0,0)}
def dfs(x,y,current_path,current_sum,visited):
    global max_sum,max_path
    if x==n-1 and y==m-1:
        if current_sum>max_sum:
            max_sum=current_sum
            max_path=current_path[:]
        return
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        tx=x+dx;ty=dy+y
        if 0<=tx<n and 0<=ty<m and (tx,ty) not in visited:
            dfs(tx,ty,current_path+[(tx,ty)],current_sum+matrix[tx][ty],visited|{(tx,ty)})
dfs(0,0,[(0,0)],matrix[0][0],v)
for i, j in max_path:
    print(i+1,j+1)