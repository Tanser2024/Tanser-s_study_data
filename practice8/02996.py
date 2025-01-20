n=int(input())
times=list(map(int,input().split()))
zipped=sorted(list(zip(times,list(range(1,n+1)))),key=lambda x:(x[0],x[1]))
s=[zipped[i][1] for i in range(n)]
t=0;dt=0
for i in range(0,n-1):
    dt+=int(zipped[i][0])
    t+=dt
t=t/n
print(" ".join(map(str,s)))
print("%.2f"%t)