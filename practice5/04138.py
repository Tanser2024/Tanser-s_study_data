def pr(n):
    dp=[1]*(n+1)
    dp[0]=dp[1]=0
    p=2
    while p*p<=n:
        if dp[p]:
            for i in range(p*p,n+1,p):
                dp[i]=0
        p+=1
    primes = [i for i in range(2, n + 1) if dp[i]]
    return primes
s=int(input())
pri=pr(s)

a=[]
for i in pri:
    if s-i in pri:
        a.append(i*(s-i))
print(max(a))