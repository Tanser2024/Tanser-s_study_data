n=int(input())
activities=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[1])
r=activities[0][1]
num=1
for i in range(1,n):
    if activities[i][0]>r:
        num+=1
        r=activities[i][1]
print(num)
