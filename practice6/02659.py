
A,B,K=map(int,input().split())
possible=[[0]*B for _ in range(A)]
num=0
nums=[-1,1]
for _ in range(K):
    r,s,p,t=map(int,input().split())
    if t==1:
        num+=1
    for i in range(r-(p-1)//2-1,r+(p-1)//2):
        for j in range(s-(p-1)//2-1,s+(p-1)//2):
            if 0<=i<A and 0<=j<B:
                possible[i][j]+=nums[t]
counts=0
for line in possible:
    counts+=line.count(num)
print(counts)
