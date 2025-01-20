import sys
sys.setrecursionlimit(999999)
direct=[(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
def dfs(x,y):
    lakes[x][y]="."
    for dx,dy in direct:
        tx=x+dx;ty=dy+y
        if lakes[tx][ty]=="W":
            dfs(tx,ty)

n,m=map(int,input().split())
lakes=[["."]*(m+2)]
for _ in range(n):
    lake=["."]+list(input())+["."]
    lakes.append(lake)
lakes.append(["."]*(m+2))
count=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if lakes[i][j]=="W":
            count+=1
            dfs(i,j)
print(count)