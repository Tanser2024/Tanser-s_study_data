
t=int(input())
n_nums=[int(input()) for _ in range(t)]
most_coins=[0]*(max(n_nums)+1)

for k in n_nums:
    for i in range(1,k+1):
        if most_coins[i]:
            continue
        if i%2==0:
            most_coins[i]=max(i-most_coins[i-1],i-most_coins[i//2])
        else:
            most_coins[i]=i-most_coins[i-1]
    print(most_coins[k])

