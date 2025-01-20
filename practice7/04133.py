d=int(input())
n=int(input())
dp=[[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,i=map(int,input().split())
    for k in range(x-d,x+d+1):
        for l in range(y-d,y+d+1):
            if 0<=k<1025 and 0<=l<1025:
                dp[k][l]+=i
num=max(max(line) for line in dp)
num1=sum(line.count(num) for line in dp)
print(num1,num)

