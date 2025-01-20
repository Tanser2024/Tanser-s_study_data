n=int(input())
data=[]
for _ in range(n):
    data.append(int(input()))
pell=[1,2]
for i in range(3,max(data)+1):
    pell.append((pell[i-2]*2+pell[i-3])%32767)
for i in data:
    print(pell[i-1])