from collections import deque

def bfs(x,y):
    stack=deque([(x,y,0)])
    v={(x,y)}
    while stack:
        x,y,s=stack.popleft()
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            tx, ty = x + dx, y + dy
            if (tx,ty) not in v :
                v.add((tx,ty))
                if matrix[tx][ty] == "0":
                    stack.append((tx,ty,s+1))
                elif matrix[tx][ty]=="1" :
                    if s!=0:
                        return s
                    else:
                        stack.appendleft((tx,ty,0))

n=int(input())
matrix=[["3"]+list(input())+["3"] for _ in range(n)]
l=len(matrix[0])
matrix=[["3"]*l]+matrix+[["3"]*l]
def solution():
    for i in range(1,n+1):
        for j in range(1,l-1):
            if matrix[i][j]=="1":
                return bfs(i,j)

print(solution())
