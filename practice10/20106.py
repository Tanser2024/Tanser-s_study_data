
import heapq

m,n,p=map(int,input().split())
matrix=[list(input().split()) for _ in range(m)]
def min_bfs(start_x,start_y,end_x,end_y):
    if matrix[start_x][start_y]=="#" or matrix[end_x][end_y]=="#":
        return "NO"
    v=set()

    q=[]
    heapq.heappush(q,(0,start_x,start_y))
    while q:
        s,x,y=heapq.heappop(q)
        if x==end_x and y==end_y:
            return s
        v.add((x,y))
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            tx,ty=x+dx,y+dy
            if (tx,ty) in v:
                continue
            if 0<=tx<m and 0<=ty<n and matrix[tx][ty]!="#":
                heapq.heappush(q,(s+abs(int(matrix[tx][ty])-int(matrix[x][y])),tx,ty))
    return "NO"
"""我们可以定义一个二维列表用来存储到达每个位置所需要的权重和，并在遇到更小的可能路径是进行更新，这样我们可以淘汰很多不是最优的jie
dist = [[float('inf')] * n for _ in range(m)]
for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and info[nr][nc] != '#':
                if dist[nr][nc] > d + abs(int(info[nr][nc]) - h):
                    dist[nr][nc] = d + abs(int(info[nr][nc]) - h)
                    heapq.heappush(pos, (dist[nr][nc], nr, nc))"""
for _ in range(p):
    start_x0,start_y0,endx,endy=map(int,input().split())
    print(min_bfs(start_x0,start_y0,endx,endy))