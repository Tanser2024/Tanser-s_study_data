import copy

def bfs(x,y,m):
    m[x][y] = (m[x][y] + 1) % 2
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        tx, ty = x + dx, y + dy
        if 0<=tx<5 and 0<=ty<6:
            m[tx][ty]=(m[tx][ty]+1)%2

def pre_process():

    for possible in q:
        possible=list(possible)

        mat1=copy.deepcopy(mat)
        if possible:
            for x,y in possible:
                bfs(x,y,mat1)
        for j in range(1, 6):
            for i in range(5):
                if mat1[i][j - 1] == 1:
                    bfs(i, j,mat1)
                    possible.append((i,j))
        if mat1==mat0:
            return possible
    return 0

mat=[list(map(int,input().split())) for _ in range(5)]
mat0=[[0]*6 for _ in range(5)]

import itertools
a=[(0,0),(1,0),(2,0),(3,0),(4,0)]
q=[[]]
for r in range(1,6):
    c=list(itertools.combinations(a,r))
    q.extend(c)


result=pre_process()

for x,y in result:
    mat0[x][y]=1
for i in range(5):
    print(*mat0[i])