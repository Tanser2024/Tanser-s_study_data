

h=int(input())
m=int(input())
time=2*h-0.5*m
projects=sorted([list(map(float,input().split())) for _ in range(m)],key=lambda x:x[0]*x[1],reverse=True)
t=[5/x[0] for x in projects]
score=0
if time>0:
    for i in range(m):
        if time>=t[i]:
            time-=t[i]
            score+=t[i]*projects[i][0]*projects[i][1]
        else:
            score+=time*projects[i][0]*projects[i][1]
            break
    print("%.1f"%score)
else:
    print(0)
