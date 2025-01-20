import bisect
# 23n2300017711(杜昌钰)
# 生成递增的字符串序列
sequence = ""
s = 0
ss = 0
sums = []


for j in range(1, 33000):
    sequence += str(j)  # 将当前数字转换为字符串并追加到序列中
    s += len(str(j))
    ss += s  # 累加当前数字的长度
    sums.append(ss)  # 将累加和添加到列表中我们其实关注的是测试用例的位置

# 处理测试用例
test_cases = int(input())

for _ in range(test_cases):
    x = int(input())

    if x == 1:
        print(1)
    else:
        # 在累加和列表中查找第一个大于等于 x 的元素
        # for i in range(len(sums)):
        #     if x <= sums[i]:
        #         # 计算偏移量并从序列中输出数字
        #         offset = x - sums[i-1] - 1
        #         print(sequence[offset])
        #         break
        i = bisect.bisect_left(sums, x)
        offset = x - sums[i - 1] - 1
        print(sequence[offset])