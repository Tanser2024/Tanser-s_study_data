n=int(input())
for _ in range(n):
    num=0
    s=int(input())
    na=int(input())
    A=list(map(int,input().split()))
    a=set(A)
    nb=int(input())
    B=list(map(int,input().split()))
    b=set(B)
    for i in a:
        if s-i in b:
            num+=B.count(s-i)*A.count(i)
    print(num)