n=int(input())
data=sorted(list(tuple(map(int,input().split())) for _ in range(n)),key=lambda x:-x[1])
min_time=0
time=0
for i in range(n):
    time+=data[i][0]
    min_time=max(min_time,time+data[i][1])
print(min_time)