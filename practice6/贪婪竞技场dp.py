def most_coins(num):
    if num<=4:
        return [0,1,1,2,3]
    dp=[0,1,1,2,3]+[0]*(num-4)
    for i in range(5,num+1):
        if i%2==0:
            dp[i]=max(dp[i//2-dp[i//2]]+i//2,dp[i-1-dp[i-1]])
        else:
            dp[i]=dp[i-1-dp[i-1]]+1
    return dp
t=int(input())
nums=[]
for _ in range(t):
    n=int(input())
    nums.append(n)
result=most_coins(max(nums))
for j in nums:
    print(result[j])


