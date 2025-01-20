def days(p,e,i,d):
    for k in range(1,925):
        a=p+23*k
        if (a-e)%28==0 and (a-i)%33==0:
            return a-d
times=0
while True:
    times+=1
    P,E,I,D=map(int,input().split())
    if P==-1:
        break
    print(f"Case {times}: the next triple peak occurs in {days(P,E,I,D)} days.")