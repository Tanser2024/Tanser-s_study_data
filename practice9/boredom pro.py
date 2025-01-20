n=int(input())
lst=list(map(int,input().split()))
l=sorted(list(set(lst)))
final_points=[l[i]*lst.count(l[i]) for i in range(len(l))]
dp=[0]*(len(l)+1)
dp[1]=final_points[0]
for i in range(2,1+len(l)):
    if l[i-1]-1 in l:
        dp[i]=max(dp[i-1],dp[i-2]+final_points[i-1])
    else:
        dp[i]=dp[i-1]+final_points[i-1]
print(dp[-1])