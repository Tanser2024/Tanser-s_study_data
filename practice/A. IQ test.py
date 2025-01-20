n=int(input())
data_list=list(map(int,input().split()))
num_1=[]
num_2=[]
x=0
for i in data_list:
    x+=1
    if i %2==0:
        num_2.append([x,i])
    else:
        num_1.append([x,i])
if len(num_1)==1:
    print(num_1[0][0])
else:
    print(num_2[0][0])
"""输出值是索引值，应该分别记录索引值和数值"""









