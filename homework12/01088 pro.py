def dfs(x,y):
    if info[x][y]>0:
        return info[x][y]
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        tx, ty = x + dx, y + dy
        if 0 <= tx < r and 0 <= ty < c and mat[tx][ty] < mat[x][y]:

r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
info=[[0]*c for _ in range(r)]