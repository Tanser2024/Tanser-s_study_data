import heapq
from collections import deque


def is_valid():
    global f
    x1,y1=start.pop()
    x2,y2=start.pop()
    q=deque([(x1,y1,x2,y2)])
    v=set()
    while q:
        x1,y1,x2,y2=q.popleft()
        v.add((x1,y1,x2,y2))
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            tx1, ty1 = x1 + dx, y1 + dy
            tx2=x2+dx;ty2=y2+dy
            if (tx1,ty1,tx2,ty2) in v:
                continue
            if 0 <= tx1 < n and 0 <= ty1 < n and 0 <= tx2 < n and 0 <= ty2 < n:
                if mat[tx1][ty1] == 1 or mat[tx2][ty2] == 1:
                    continue
                if mat[tx1][ty1] == 9 or mat[tx2][ty2] == 9:
                    f = True
                    return
                q.append((tx1, ty1, tx2, ty2))
    return
n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
start=[]
end=[]

for i in range(n):
    if len(start)==2 and len(end)==1:
        break
    for j in range(n):
        if mat[i][j]==5:
            start.append((i,j))
        elif mat[i][j]==9:
            end.append((i,j))
        if len(start)==2 and len(end)==1:
            break
f=False
is_valid()
if f:
    print("yes")
else:
    print("no")

