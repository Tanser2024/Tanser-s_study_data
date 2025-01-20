n,k,d=map(int,input().split())
def max_num(n,k):
    if k==0:
        return 0
    dp=[0]*(n+1)
    dp[0]=1
    num=1
    for i in range(1,n+1):
        if i<k+1:
            dp[i]=num%1000000007
            num*=2
        else:
            dp[i]=(2*dp[i-1]-dp[i-k-1])%1000000007
    return dp[-1]
#一行这套算法实际上计算的是对整数n，将其分解为不超过k的整数有多少种分法，因此再减去max_num(n,d-1)即可得到子整数不小于d且不超过k的所有可能分法
print((max_num(n,min(k,n))-max_num(n,d-1))%1000000007)



