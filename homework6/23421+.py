n, W = map(int, input().split())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))
dp = [0] * (W + 1)

for i in range(n):
    for j in range(W, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

print(dp[W])