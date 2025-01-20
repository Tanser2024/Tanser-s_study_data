n=int(input())
money=input().split()
money_rank=sorted([int(x) for x in money])
num=0
coins=0
s=sum(money_rank)
for i in range(n):
    num+=1
    coins+=money_rank[n-1-i]
    if coins>s/2:
        break
print(num)

