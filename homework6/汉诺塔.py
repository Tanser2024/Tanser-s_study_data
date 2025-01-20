def han(num,times,steps,a,b,c):
    if num==1:
        steps.append([a,c])
        return times+1
    else:
        times=han(num-1,times,steps,a,c,b)
        steps.append([a,c])
        times=han(num-1,times+1,steps,b,a,c)
        return times
n=int(input())
t=0
s=[]
a0="A"
b0="B"
c0="C"
t=han(n,t,s,a0,b0,c0)
print(t)
for i in s:
    print("->".join(i))