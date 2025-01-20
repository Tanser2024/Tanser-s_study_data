def kill_time(skills,m,b):
    num=0
    t=skills[0][0]
    for skill in skills:
        if skill[0]==t:
            num+=1
        else:
            t=skill[0]
            num=1
        if num<=m:
            b-=skill[1]
        if b<=0:
            return t
    return "alive"
cases=int(input())
for _ in range(cases):
    n,M,B=map(int,input().split())
    s=[list(map(int,input().split())) for _ in range(n)]
    s.sort(key=lambda x:(x[0],-x[1]))
    print(kill_time(s,M,B))