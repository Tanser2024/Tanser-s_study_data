T,n=map(int,input().split())
pract=[]
for _ in range(n):
    t,w=map(int,input().split())
    pract.append((t,w))
pract.sort(key=lambda x:-x[0])
dp=[-1]*(T+1)
dp[0]=0
for j in range(n):

    for i in range(T,pract[j][0]-1,-1):
        if dp[i-pract[j][0]]>=0:
            dp[i]=max(dp[i],dp[i-pract[j][0]]+pract[j][1])
print(dp[-1])

