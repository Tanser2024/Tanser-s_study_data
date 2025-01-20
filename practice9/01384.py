def min_value(coin,w):
    dp=[float("inf")]*(w+1)
    dp[0]=0
    for i in range(w+1):
        for j in range(len(coin)):
            if coin[j][1]<=i:
                dp[i]=min(dp[i-coin[j][1]]+coin[j][0],dp[i])
    if dp[-1]!=float("inf"):
        print(f"The minimum amount of money in the piggy-bank is {dp[-1]}.")
    else:
        print("This is impossible.")


t=int(input())
for _ in range(t):
    w0,w1=map(int,input().split())
    W=w1-w0
    coins=[]
    n=int(input())
    for _ in range(n):
        value,weight=map(int,input().split())
        coins.append((value,weight))
    min_value(coins,W)
