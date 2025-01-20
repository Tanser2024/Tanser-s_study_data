

def sai(tian,king,num):
    money=0
    i=0;j=0;k=num-1;l=num-1
    while True:
        if tian[k]>king[l]:
            k-=1;l-=1;money+=200
        elif tian[i]>king[j]:
            i+=1;j+=1;money+=200
        else:
            if tian[i]==tian[k]==king[j]==king[l]:
                return money
            else:
                i+=1;l-=1;money-=200
        if i>k:
            break
    return money

while True:
    n=int(input())
    if n==0:
        break
    t=sorted(list(map(int,input().split())))
    k=sorted(list(map(int,input().split())))
    print(sai(t,k,n))