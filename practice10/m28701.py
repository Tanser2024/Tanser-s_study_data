n,k=map(int,input().split())
time=sorted(list(map(int,input().split())))
dp=[[0]*(n+1) for _ in range(k)]
s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=s[i-1]+time[i-1]
dp[k]=time[0]
for j in range(k+1,n+1):
    if time[j-1]*(k-1)<=s[j-1]:
        dp[j]=dp[j-1]+time[j-1]/k
    else:
        dp[j]=dp[j-1]+s[j-1]/(k*(k-1))
print("%.3f"%dp[-1])
