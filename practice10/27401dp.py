a,b=map(int,input().split())
price=list(map(int,input().split()))
s=sum(price)
dp=[float("inf")]*(s+1)
dp[0]=0
for p in price:
    for j in range(len(dp)-1,p-1,-1):
        dp[j]=min(dp[j-p]+p,dp[j])

for j in range(b,s+1):
    if dp[j]>=b and dp[j]!=float("inf"):
        print(dp[j])
        exit()
print(0)