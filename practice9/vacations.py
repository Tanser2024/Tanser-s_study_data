

n=int(input())
activities=list(map(int,input().split()))
if n==1:
    print(activities.count(0))
    exit()

for i in range(1,n):
    if activities[i]==activities[i-1] and activities[i] in {1,2}:
        activities[i]=0
    if activities[i]==3:
        if activities[i-1]==2:
            activities[i]=1
        elif activities[i-1]==1:
            activities[i]=2

print(activities.count(0))


