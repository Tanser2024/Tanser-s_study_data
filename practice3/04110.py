n,w=map(int,input().split())
lst=[]
lst_pr=[]
for _ in range(n):
    va,we=map(int,input().split())
    pri=va/we
    lst.append([va,we,pri])
    lst_pr.append(pri)
value=0
weight=0
while True:
    a=lst_pr.index(max(lst_pr))
    if weight+lst[a][1]<w:
        weight += lst[a][1]
        value += lst[a][0]
        del lst[a]
        del lst_pr[a]
    else:
        break
value+=(w-weight)*max(lst_pr)
print("%.1f\n"%value)