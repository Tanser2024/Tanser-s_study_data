def is_valid(num,m):
    if not num:
        return "No"
    if any(x==m for x in num):
        return "Yes"
    num={2*x//3 for x in num if 2*x%3==0}|{x//3 for x in num if x%3==0}
    return is_valid(num,m)
t=int(input())
for _ in range(t):
    n,M=map(int,input().split())
    N={n}
    print(is_valid(N,M))