from bisect import bisect_right
n=int(input())
shops_price=sorted(list(map(int,input().split())))
q=int(input())
money=[int(input()) for _ in range(q)]
for i in range(q):
    print(bisect_right(shops_price,money[i]))
