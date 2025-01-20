n,m=map(int,input().split())
coins=sorted(list(map(int,input().split())))
dp=[-1]*(m+1)
d=[False]*(m+1)
for i in coins:
    dp[i]=1
    d[i]=True
for i in range(m+1):
    for j in range(n):
        if i>=coins[j] and d[i-coins[j]] :
            if d[i]:
                dp[i]=min(dp[i],dp[i-coins[j]]+1)
            else:
                dp[i]=dp[i-coins[j]]+1
            d[i]=True
print(dp[m])