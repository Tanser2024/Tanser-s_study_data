n=int(input())
for _ in range(n):
    a,b,c=map(float,input().split())
    det= b*b-4*a*c
    if b==0:
        b=-b
    if det>0:
        x1=(-b+det**0.5)/(2*a)
        x2=(-b-det**0.5)/(2*a)
        if a<0:
            x1,x2=x2,x1
        print("x1=%.5f;x2=%.5f"%(x1,x2))
    elif det==0:
        x1=-b/(2*a)
        print("x1=x2=%.5f"%x1)
    else:
        x=-b/(2*a)
        x1i=(-det)**0.5/(2*a)
        if a>0:
            print("x1=%.5f+%.5fi;x2=%.5f-%.5fi"%(x,x1i,x,x1i))
        else:
            print("x1=%.5f+%.5fi;x2=%.5f-%.5fi"%(x,-x1i,x,-x1i))