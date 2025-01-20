def wiggleMaxLength(self, nums):
    if len(nums) == 1:
        return 1
    dp = [5] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 0:
            dp[i] = 1
        elif nums[i] - nums[i - 1] < 0:
            dp[i] = -1
    l=0
    for i in range(1, len(nums)):
        if dp[i] == 1 or dp[i] == -1:
            flag = dp[i]
            l = 2
            break
    if not l:
        for i in range(1, len(nums)):
            if dp[i] + flag == 0:
                flag = dp[i]
                l += 1
        return l
    else:
        return 1
