a=list(map(int,input().split()))
money=0

max_m=[0]*len(a)
max_m[-1]=a[-1]
if len(a)==1:
    print(0)
    exit()
for i in range(len(a)-2,-1,-1):
    max_m[i]=max(max_m[i+1],a[i])
for i in range(0,len(a)):
    money=max(money,max_m[i]-a[i])
print(money)