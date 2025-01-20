m,n,p,q=map(int,input().split())
mn=[]
pq=[]
outputs=[]
for _ in range(m):
    mn.append(list(map(int,input().split())))
for _ in range(p):
    pq.append(list(map(int,input().split())))
for i in range(m+1-p):
    outs=[]
    for j in range(n+1-q):
        l=i
        out=0
        for a in range(p):
            k=j
            for b in range(q):
                out+=mn[l][k]*pq[a][b]
                k+=1
            l+=1
        outs.append(out)
    outputs.append(outs)
for out in outputs:
    print(" ".join(map(str,out)))
