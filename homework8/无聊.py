def max_points(nums):
    if not nums:
        return 0
    freq = [0] * 100001
    for num in nums:
        freq[num] += 1
    dp = [0] * 100001
    dp[1] = freq[1]
    for i in range(2, 100001):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])
    return dp[100000]
n = int(input())
nums = list(map(int, input().split()))
print(max_points(nums))