price=list(map(int,input().split(",")))
l=len(price)
if l==1:
    print(price[0])
    exit()
max_m=[-float("inf")]*l
max_m[-1]=max(0,price[-1])
for i in range(l-2,-1,-1):
    max_m[i]=max(0,max_m[i+1]+price[i],price[i])
min_m=max(0,price[0])
money=-float("inf")
for j in range(1,l-1):

    money=max(max_m[j+1]+min_m,price[j]+max_m[j+1]+min_m,money)
    min_m=max(0,min_m+price[j],price[j])

print(money)
