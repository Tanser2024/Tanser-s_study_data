
def dfs(x,y):
    max_s=0
    stack=[(x,y,1)]
    while stack:
        x,y,s=stack.pop()
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            tx,ty=x+dx,y+dy
            if 0<=tx<r and 0<=ty<c and mat[tx][ty]<mat[x][y]:
                stack.append((tx,ty,s+1))
        max_s=max(s,max_s)
        if max_s==r*c:
            return max_s
    return max_s

r,c=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(r)]
longest_s=1
for i in range(r):
    for j in range(c):
        if all(mat[i][j]>=mat[i+dx][j+dy] for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)] if 0<=i+dx<r and 0<=j+dy<c):
            longest_s=max(longest_s,dfs(i,j))
            if longest_s==r*c:
                print(longest_s)
                exit()
print(longest_s)
