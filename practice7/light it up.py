n,time=map(int,input().split())
times=[0]+list(map(int,input().split()))+[time]
initial_on_time=[]
initial_off_time=[0]
t_on=0
t_off=0
for i in range(2,len(times),2):
    t_off += times[i] - times[i - 1]
    initial_off_time.append(t_off)
for i in range(1,len(times),2):
    t_on+=times[i]-times[i-1]
    initial_on_time.append(t_on)
t=initial_on_time[-1]
for i in range(len(initial_on_time)):
    t=max(t,initial_on_time[i]+initial_off_time[-1]-initial_off_time[i]-1)
print(t)



