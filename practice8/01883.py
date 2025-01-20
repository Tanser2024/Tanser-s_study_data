def k_lst(lst,k):
    t=-3
    if k==0:
        return lst
    for i in range(len(lst)-1,0,-1):
        if lst[i]>lst[i-1]:
            t=i-1
            break
    if t==-3:

        return k_lst(lst[::-1],k-1)
    n=t+1
    for j in range(t,len(lst)):
        if lst[j]>lst[t]:
            n=j
    lst[t],lst[n]=lst[n],lst[t]
    lst[t + 1:] = lst[t + 1:][::-1]
    return k_lst(lst,k-1)
m=int(input())
for _ in range(m):
    num,ki=map(int,input().split())
    l=list(map(int,input().split()))
    result=k_lst(l,ki)
    print(*result)