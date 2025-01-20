num,shop=map(int,input().split())
price=[];q_x=[]
for _ in range(num):
    price.append(list(input().split()))
for _ in range(shop):
    q_x.append(list(input().split()))#有n家
possible_cost=[[0]*num for _ in range(shop)]
for i in range(num):
    for data in price:
        for j in range(len(data)):
            n,p=map(int,data[j].split(":"))
            possible_cost[n-1][i]=p


