def exits(x):
    x=int(x)
    pr=[0]*(x+1)
    for i in range(1,x+1):
        m=i
        while m <=x:
            if pr[m]==0:
                pr[m]=1
            else:
                pr[m]=0
            m+=i
    num=pr.count(1)


    print(num)

n=int(input())
lst=[input() for _ in range(n)]
for k in lst:
    exits(k)