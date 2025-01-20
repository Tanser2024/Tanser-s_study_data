n,l=map(int,input().split())
sets=sorted(list(map(int,input().split())))
if len(sets)==1:
    d=max(sets[0],l-sets[0])
else:
    le=[sets[i]-sets[i-1] for i in range(1,n)]
    d1=max(le)/2
    d2=sets[0]
    d3=l-sets[-1]
    d=max(d1,d2,d3)
print("%.12f"%d)