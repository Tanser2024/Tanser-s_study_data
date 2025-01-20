n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[1]*n
A={a[-1]}
if n==1:
    for i in range(m):
        print(1)
    exit()
for i in range(n-2,-1,-1):
    if a[i] not in A:
        dp[i]=dp[i+1]+1
        A.add(a[i])
    else:
        dp[i]=dp[i+1]
for _ in range(m):
    t=int(input())
    print(dp[t-1])