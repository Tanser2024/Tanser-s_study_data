n=int(input())
s=[i for i in range(1,n+1)]
out=[]
buff=[]
def lis(a,b,buffer):
    if len(a)==1:
        b.append(buffer+a)
    else:
        for i in range(len(a)):
            a[0],a[i]=a[i],a[0]
            lis(a[1:],b,buffer+[a[0]])
lis(s,out,buff)
for i in out:
    print(" ".join(map(str,i)))






