n=int(input())
ma=[list(map(int,input()))for _ in range(n)]
m,dire=len(ma[0]),[(1,0),(-1,0),(0,1),(0,-1)]
for i in range(n):
    for j in range(m):
        if ma[i][j]==1 :
            xl,yl=i,j
import heapq
def dijkstra(x,y):
    q,visited=[],[[False]*m for _ in range(n)]
    heapq.heappush(q,(0,x,y))
    while q:
        step,x,y=heapq.heappop(q)
        if visited[x][y]:
            continue
        visited[x][y]= True
        if ma[x][y]==1 and step!=0:
            return step

        for dx,dy in dire:
            if 0<=x+dx<n and 0<=y+dy<m and not visited[x+dx][y+dy]:
                heapq.heappush(q,(step+1-ma[x+dx][y+dy],x+dx,y+dy ))
print(dijkstra(xl,yl))
