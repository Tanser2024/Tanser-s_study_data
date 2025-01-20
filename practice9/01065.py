from bisect import bisect_left
def max_smaller(lst):
    lis=[]
    for i in lst:
        pos=bisect_left(lis,i)
        if pos<len(lis):
            lis[pos]=i
        else:
            lis.append(i)
    return len(lis)

t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    d=sorted([(data[i],data[i+1]) for i in range(0,2*n-1,2)],key=lambda x:(x[0],x[1]))
    l=[d[i][1] for i in range(n-1,-1,-1)]
    print(max_smaller(l))