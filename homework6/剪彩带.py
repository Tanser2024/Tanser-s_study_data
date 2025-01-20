def max_ribbon_pieces(n, a, b, c):
    # 初始化 dp 数组，dp[i] 表示长度为 i 的丝带可以切成的最大数量
    dp = [-1] * (n + 1)
    dp[0] = 0  # 长度为 0 的丝带可以切成 0 段

    # 填充 dp 数组
    for i in range(1, n + 1):
        if i >= a and dp[i - a] != -1:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i >= b and dp[i - b] != -1:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i >= c and dp[i - c] != -1:
            dp[i] = max(dp[i], dp[i - c] + 1)

    return dp[n]

# 读取输入
n, a, b, c = map(int, input().split())

# 计算并输出结果
print(max_ribbon_pieces(n, a, b, c))