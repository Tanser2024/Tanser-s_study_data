n,q=map(int,input().split())
pair=[]
for _ in range(q):
    x,y=map(int,input().split())
    pair.append((x,y))
num=0
for x,y in pair:
    if (y,x) in pair:
        print("Yes")
        break
    num+=1
if num==q:
    print("No")