lucky=[4,7,47,74,447,474,477]
n=int(input())
num=0
for i in lucky:
    if n%i==0:
        num+=1
if n in [744,747,777]:
    num+=1
if num>=1:
    print("YES")
else:
    print("NO")
