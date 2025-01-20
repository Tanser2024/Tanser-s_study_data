s=list(input())
l=1
length=[]
if len(s)>1:
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            l+=1
        else:
            length.append(l)
            l=1
    print(max(length))
else:
    print("1")