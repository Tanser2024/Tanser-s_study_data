p=int(input())
values=sorted(list(map(int,input().split())))
num=0
def max_num(m,v,n):
    if len(v)==1:
        if m>=v[0]:
            return n+1
        else:
            return n
    else:
        if m>=v[0]:
            return max_num(m-v[0], v[1:], n+1)
        elif m<v[0] and n>0:
            return max_num(m+v[-1],v[:-1],n-1)
        else:
            return n
print(max_num(p,values,num))