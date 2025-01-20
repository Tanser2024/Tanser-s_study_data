"""
至少需要n个筹码
每个筹码可覆盖一行一列
则至少需要n个筹码实现全覆盖
就不需要n+1筹码
在这样的前提下，意味着a中所有元素被取出 或者b
"""
def min_pain(n):
    n=int(n)
    a=[int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(min(sum(a)+min(b)*n,sum(b)+min(a)*n))
t=int(input())
for _ in range(t):
    num=input()
    min_pain(num)