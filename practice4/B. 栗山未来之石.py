def pro_1(l,r,sums):
    value1=sums[r]-sums[l-1]
    return value1
def pro_2(l,r,sums):
    value2=sums[r]-sums[l-1]
    return value2
n=int(input())
data1=list(map(int,input().split()))
data2=sorted(data1)
sums1=[0]
sums2=[0]
for i in range(n):
    sums1.append(sums1[i]+data1[i])
for i in range(n):
    sums2.append(sums2[i]+data2[i])
for _ in range(int(input())):
    inputs=list(map(int,input().split()))
    if inputs[0]==1:
        print(pro_1(inputs[1],inputs[2],sums1))
    else:
        print(pro_2(inputs[1], inputs[2],sums2))