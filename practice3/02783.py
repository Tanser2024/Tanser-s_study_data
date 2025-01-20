while True:
    n=int(input())
    data=[]
    if n==0:
        break
    for _ in range(n):
        a,b=map(int,input().split())
        data.append([a,b])
    data.sort()
    data1=[x[1] for x in data]
    m=1
    data2=[data1[0]]
    for i in range(1,n):
        if data1[i]<min(data2):
            m+=1
            data2.append(data1[i])
    print(m)


