while True:
    n,m=map(int,input().split())
    if n==0:
        break
    dp=[0]*(m+1)
    dp[0]=1
    lst=list(map(int,input().split()))
    for i in range(n):
        for j in range(lst[i],m+1):
            if  0<lst[n+i] and dp[j-lst[i]]>0:
                dp[j]+=1
                lst[n+i]-=1
    print(m-dp.count(0))
    print(dp)