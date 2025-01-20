n=int(input())
a=list(map(int,input().split()))
s=[0]*n
s[0]=a[0]
for i in range(1,n):
    s[i]=s[i-1]+a[i]
if s[n-1]%3!=0 or n<3:
    print(0)
else:
    c=s[n-1]//3*2
    b=s[n-1]//3
    num=0
    count=0
    if s[n-1]!=0:
        for i in range(n-1):
            if s[i]==b:
                count+=1
            if s[i]==c:
                num+=count
    else:
        q=s[:n-1].count(0)
        num=q*(q-1)//2
    print(num)
