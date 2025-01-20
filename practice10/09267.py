n,m=map(int,input().split())
dp=[1]*(n+1)
if n<m:
    print(2**n)
    exit()
for i in range(1,m):
    dp[i]=2**i
dp[m]=2**m-1
for i in range(m,n):
    dp[i+1]=2*dp[i]-dp[i-m]
print(dp[-1])