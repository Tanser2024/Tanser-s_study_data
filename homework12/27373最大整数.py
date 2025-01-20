m=int(input())
n=int(input())
nums=sorted(list(map(str,input().split())) , key=lambda x:(x*20)[:20] ,reverse=True)
#逻辑的难点在于为什么这样排序，也就是为什么采用这样的贪心策略
#如果直接进行动态规划，不能保证无后效性，如果num位于两个数中间时值最大，那么就不能得到最优解
#而这样排序后，每次加上的数字都可以保证是符合条件下最大的可能
dp=[""]*(m+1)

for num in nums:
    l=len(num)
    for i in range(m,l-1,-1):
        if dp[i]=="":
            dp[i]=dp[i-l]+num
        dp[i]=str(max(int(dp[i]),int(dp[i-l]+num)))
print(dp[-1])