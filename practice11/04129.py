
import heapq
def dijkstra(x,y,k):

    q=[]
    heapq.heappush(q,(0,x,y))
    visited[0][x][y] = True
    while q:
        t,x,y=heapq.heappop(q)
        for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
            tx,ty=x+dx,y+dy
            if 0<=tx<r and 0<=ty<c and not visited[(t+1)%k][tx][ty]:
                """if mat[tx][ty]=="." or ((t+1)%k==0 and mat[tx][ty]=="#"):
                    visited[(t + 1) % k][tx][ty]=True
                    heapq.heappush(q,(t+1,tx,ty))
                    这种情况下，mat[tx][ty]=="E 不会进入q中，也就不会return t+1
                    因此任何情况下都只会输出“Oop！”
                   if mat[tx][ty]=="E":
                        return t+1"""
                if mat[tx][ty] != "#" or ((t + 1) % k == 0 and mat[tx][ty] == "#"):
                    visited[(t + 1) % k][tx][ty] = True
                    heapq.heappush(q, (t + 1, tx, ty))
                if mat[tx][ty] == "E":
                    return t + 1
    return "Oop!"

T=int(input())
for _ in range(T):
    r,c,k=map(int,input().split())
    mat=[list(input()) for _ in range(r)]
    visited=[[[False]*c for _ in range(r)] for _ in range(k)]
    for i in range(r):
        for j in range(c):
            if mat[i][j]=="S":
                print(dijkstra(i,j,k))
