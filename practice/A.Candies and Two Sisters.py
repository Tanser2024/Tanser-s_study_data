t=int(input())
for i in range(t):
    n=int(input())
    if n>2:
        print((n-1)//2)
    else:
        print(0)
"""t = int(input())

for _ in range(t):
    n = int(input())
    print((n - 1) // 2 if n > 2 else 0)"""
"""# 读取测试用例数量
t = int(input())

# 读取所有测试用例
test_cases = [int(input()) for _ in range(t)]

# 计算每个测试用例的结果
results = [(n - 1) // 2 if n > 2 else 0 for n in test_cases]

# 输出结果
for result in results:
    print(result)"""