def josephus(n, m):
    if n == 1:
        return 0
    else:
        # 递归调用，并根据m调整位置
        return (josephus(n - 1, m) + m) % n
while True:
    n,m=map(int,input().split())
    if n==0:
        break
    print(josephus(n,m)+1)

