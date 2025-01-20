def min_num(m, p, r):
    if m % 50 != 0:
        return "Fail"
    m = m // 50
    dp = [float('inf')] * (m + 1)
    dp[0] = 0  # 支付金额 0 所需的球票数为 0

    for i in range(6, -1, -1):
        cur = p[i]
        for k in range(m, cur - 1, -1):
            for j in range(1, r[i] + 1):
                if k >= cur * j:
                    dp[k] = min(dp[k], dp[k - cur * j] + j)
                else:
                    break

    if dp[-1] == float('inf'):
        return "Fail"
    else:
        return dp[-1]

# 读取输入
money = int(input())
price = [1, 2, 5, 10, 20, 50, 100]
rest = list(map(int, input().split()))

# 输出结果
print(min_num(money, price, rest))