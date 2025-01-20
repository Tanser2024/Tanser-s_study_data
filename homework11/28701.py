n,k=map(int,input().split())
time=sorted(list(map(int,input().split())))
total_time=sum(time)
for i in range(n):
    if time[n-1-i]*k>total_time:
        total_time-=(time[n-1-i])
        k-=1
    else:
        break
print("%.3f"%(total_time/k))