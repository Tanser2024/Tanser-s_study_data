def min_tests(tasks):
    num=1
    r=tasks[0][1]
    for task in tasks:
        if task[0]<=r:
            r=min(r,task[1])
        else:
            r=task[1]
            num+=1
    return num
k=int(input())
for _ in range(k):
    n=int(input())
    t=[]
    for _ in range(n):
        t.append(list(map(int,input().split())))
    print(min_tests(sorted(t)))