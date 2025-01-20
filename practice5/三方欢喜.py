n,q=map(int,input().split())
likes=[]
for _ in range(q):
    likes.append(list(map(int,input().split())))
num=0
for like in likes:
    if any([like[1],j] in likes and [j,like[0]] in likes for j in range(1,n+1)):
        print("Yes")
        break
    else:
        num+=1
if num==q:
    print("No")