"""a,b,c,d=input().split()
if a>c and int(b)>=22 and int(d)>=20:
    print("legal")
elif a<c and int(b)>=20 and int(d)>=22:
    print("legal")
else:
    print("illegal")"""
n,m=map(int,input().split())
sales=input().split()
sale=sorted([int(i) for i in sales])
come=0
for i in range(m):
    if sale[i] <0:
        come+=sale[i]
print(int(-come))

