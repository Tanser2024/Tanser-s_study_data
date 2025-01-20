n,b=map(int,input().split())
value=list(map(int,input().split()))
weight=list(map(int,input().split()))
flag=[[True]*n for _ in range(b+1)]
dp=[0]*(b+1)
for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+value[i])

print(dp[-1])