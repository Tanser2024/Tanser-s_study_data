dp=[True]*(1000000+1)
dp[0]=dp[1]=False
prime=[]
for i in range(2,1000001):
    if dp[i]:
        prime.append(i)
    for p in prime:
        if i*p>=1000001:
            break
        dp[i*p]=False
        if i%p==0:
            break
n=int(input())
ans=0
for p in prime:
    if n%p==0:
        ans+=1
        if n%(p*p)==0:
            print(0)
            exit()
if ans%2==0:
    print(1)
else:
    print(-1)
