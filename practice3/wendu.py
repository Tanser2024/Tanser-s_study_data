"""a=input()
if a[-1]=="F":
    b=float(a[0:-1])#保留数字部分
    c=(b-32)/1.8

else:
    c=float(a[0:-1])+273.15
print("%.2fC"%c)#只有字符串能拼接"""
"""n=int(input())
s=0
for _ in range(n):
    s+=int(input())
print("%.5f"%s/n)"""
"""is_prime=[True]*100
n=50
primes=[]
i = 2
if is_prime[i]:
    primes.append(i)  # 将 2 加入 primes 列表
    for p in primes:
        if p * i > n:
            break
        print(f"标记 {p} * {i} = {p * i} 为合数")
        is_prime[p * i] = False  # 标记合数
        if i % p == 0:
            break"""


def euler_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

        for p in primes:
            if p * i > n:
                break
            is_prime[p * i] = False
            if i % p == 0:
                break

    return primes, is_prime


# 示例
n = 30
primes, is_prime = euler_sieve(n)
print(f"素数列表: {primes}")
print(f"is_prime 数组: {is_prime}")
