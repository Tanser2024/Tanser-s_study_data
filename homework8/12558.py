def length_of_island(map_of_island,n,m):
    length=0
    for i in range(n):
        for j in range(m):
            if map_of_island[i][j]==1:
                for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                    if 0<=i+dy<n and 0<=j+dx<m:
                        if map_of_island[i+dy][j+dx]==0:
                            length+=1
                    else:
                        length+=1
    return length
N,M=map(int,input().split())
island=[list(map(int,input().split())) for _ in range(N)]
print(length_of_island(island,N,M))
