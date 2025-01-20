
t,k=map(int,input().split())
dp=[1]*100001
for n in range(100001):
    if n>=k:
        dp[n]=(dp[n-1]+dp[n-k])%1000000007
for i in range(100001):
    dp[i]=(dp[i-1]+dp[i])%1000000007
for _ in range(t):
    s,r=map(int,input().split())
    print((dp[r]-dp[s-1])%1000000007)