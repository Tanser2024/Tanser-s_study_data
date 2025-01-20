t=0
from collections import deque
def bfs(x,y):
    global total_step
    visited=set()
    stack=deque([(x,y,1,0)])
    while stack:
        x,y,step,s=stack.popleft()
        visited.add((x,y))
        for dx,dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            tx,ty=x+dx,y+dy
            if dx==0:
                new_s=1
            else:
                new_s=-1
            if 0<=tx<=w+1 and 0<=ty<=h+1 and (tx,ty) not in visited :
                if (tx,ty)==target:
                    if s+new_s==0:
                        total_step=min(total_step,step+1)
                    elif abs(s+new_s)==2 or abs(s+new_s)==1:
                        total_step = min(total_step, step )
                    continue
                if matrix[ty][tx]==" ":
                    if s+new_s==0:
                        stack.append((tx,ty,step+1,new_s))
                    elif  abs(s + new_s) == 2 or abs(s+new_s)==1:
                        stack.append((tx, ty, step, new_s))
while True:
    t+=1
    w,h=map(int,input().split())
    if w==h==0:
        break
    matrix=[[" "]*(w+2)]+[[" "]+list(input())+[" "] for _ in range(h)]+[[" "]*(w+2)]
    data=[];k=0
    print(f"Board #{t}:")
    while True:
        k+=1
        l=list(map(int,input().split()))
        if l[0]==l[1]==l[2]==l[3]==0:
            break
        total_step = float("inf")
        target = (l[2], l[3])
        bfs(l[0], l[1])
        print(f"Pair {k}: {total_step} segments." if total_step != float("inf") else f"Pair {k}: impossible.")
    print()