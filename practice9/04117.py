import sys
input = sys.stdin.read
data = input().split()
data=[int(x) for x in data]
n=max(data)
dp=[[1]*(n+1) for _ in range(n+1)]
for i in range(2,n+1):
    for j in range(2,n+1):
        if j>i:
            dp[i][j]=dp[i][j-1]
        else:
            dp[i][j]=dp[i][j-1]+dp[i-j][j]
for a in data:
    print(dp[a][a])

