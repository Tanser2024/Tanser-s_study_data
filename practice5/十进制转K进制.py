n,K=map(int,input().split())
k=K
N=n
a=[]
while K<=k*N:
    a.append(int(n%k))
    n=(n-n%k)/k
    K=K*k
dic={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
b=[dic[i] for i in reversed(a)]
print("".join(map(str,b)))
