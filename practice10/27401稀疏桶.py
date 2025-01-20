# 稀疏桶
a, b = map(int, input().split())
c = {0}
for i in map(int, input().split()):
    for j in c.copy():#否则i+j也可能在对同一个i下被再次取出，导致价值为i的商品购买了两件
        if j < b: c.add(i + j)
for i in sorted(c):
    if i >= b: print(i);exit()
print(0)


