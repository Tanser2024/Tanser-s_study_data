k=int(input())
h=list(map(int,input().split()))
dp=[1]*k
for i in range(k):
    for j in range(i):
        if h[j]>=h[i]:
            dp[i]=max(dp[j]+1,dp[i])
print(max(dp))

