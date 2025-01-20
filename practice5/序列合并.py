n,m=input().split()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
print(" ".join(map(str,sorted(c))))