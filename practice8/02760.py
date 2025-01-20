def max_sum(matrix,n,mat):
    matrix[0][0]=mat[0][0]
    matrix[1][0]=matrix[0][0]+mat[1][0]
    matrix[1][1]=matrix[0][0]+mat[1][1]
    if n==2:
        return max(matrix[1])
    for i in range(2,n):
        for j in range(1,i):
            matrix[i][j]=max(matrix[i-1][j-1],matrix[i-1][j])+mat[i][j]
        matrix[i][0]=matrix[i-1][0]+mat[i][0]
        matrix[i][-1]=matrix[i-1][-1]+mat[i][-1]
    return max(matrix[-1])
N=int(input())
M=[[0]*i for i in range(1,N+1)]
m=[list(map(int,input().split())) for _ in range(N)]
print(max_sum(M,N,m))