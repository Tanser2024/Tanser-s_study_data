n,m,k=map(int,input().split())
data=[tuple(map(int,input().split())) for _ in range(k)]
dp=[[0]*(m+1) for _ in range(n+1)]
rest_m=[[m]*(m+1) for _ in range(n+1)]
for d in data:
    for i in range(n,d[0]-1,-1):
        for j in range(m,d[1]-1,-1):
            cur=dp[i][j]
            dp[i][j]=min(max(dp[i-d[0]][j]+1,dp[i][j]),max(dp[i][j-d[1]]+1,dp[i][j]))
            if dp[i][j]>cur:
                rest_m[i][j]=rest_m[i-d[0]][j-d[1]]-d[1]
            else:
                rest_m[i][j]=rest_m[i-d[0]][j-d[1]]
print(dp[-1][-1],rest_m[-1][-1])

