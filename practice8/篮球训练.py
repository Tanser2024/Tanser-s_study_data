n=int(input())
stu1=list(map(int,input().split()))
stu2=list(map(int,input().split()))
dp=[0]*n
DP=[0]*n
dp[0]=stu1[0]
DP[0]=stu2[0]
for i in range(1,n):
    dp[i]=max(DP[i-1]+stu1[i],dp[i-1])
    DP[i]=max(dp[i-1]+stu2[i],DP[i-1])
print(max(dp[-1],DP[-1]))