n=int(input())
data=[]
for a1 in range(n+1):
    for a2 in range(n+1):
        for a3 in range(n+1):
            if (a1+a2)%2==0 and (a2+a3)%3==0 and (a1+a2+a3)%5==0:
                data.append(a1+a2+a3)
print(max(data))