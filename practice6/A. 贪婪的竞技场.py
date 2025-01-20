def most_coins(n,coins):
    if n==0:
        return coins
    if n==1:
        return coins+1
    if n%2==0:
        if n%4==0 and n>4:
            return most_coins(n-2,coins+1)
        else:
            return most_coins(n//2-1,coins+n//2)
    else:
        if (n-1) % 4 == 0 and (n-1 )> 4:
            return most_coins(n - 2, coins + 1)
        else:
            return most_coins((n-1) // 2, coins + 1)
t=int(input())
for i in range(t):
    N=int(input())
    c=0
    print(most_coins(N,c))