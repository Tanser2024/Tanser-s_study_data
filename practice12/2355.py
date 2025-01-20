n=int(input())
total=set(range(1,n+1))
a=list(map(int,input().split()))
rest=set()
others=[]
for i in a:
    if i<=n:
        rest.add(i)
    else:
        others.append(i)
b=sorted(list(total-rest))
others.sort()
print(*b)
print(*others)
