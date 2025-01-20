"""s=input()
dp=[0]*len(s)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        dp[i]=1
m=int(input())
for _ in range(m):
    l,r=map(int,input().split())
    print(dp[l-1:r-1].count(1))"""
s = input()
n = len(s)
# 初始化前缀和数组
prefix_sum = [0] * (n + 1)

# 计算前缀和
for i in range(n - 1):
    if s[i] == s[i + 1]:
        prefix_sum[i + 1] = prefix_sum[i] + 1
    else:
        prefix_sum[i + 1] = prefix_sum[i]

m = int(input())
# 处理每个查询
for _ in range(m):
    l, r = map(int, input().split())
    # 直接通过前缀和数组计算查询区间的和
    print(prefix_sum[r - 1] - prefix_sum[l - 1])
