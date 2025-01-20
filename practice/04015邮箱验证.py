import sys
def is_or_not(spring):
    num=0
    for i in spring:
        if i == "@":
            num+=1
    if num==1:
        if spring[0]in{"@","."}or spring[-1] in {"@","."}:
            print("NO")
        else:
            if "." in spring[spring.index("@"):] :
                lst=[inde for inde,x in enumerate(spring) if x == "."]
                if spring.index("@")+1 not in lst  and spring.index("@")-1 not in lst:
                    print("YES")

                else:
                    print("NO")
            else:
                print("NO")


    else:
        print("NO")
lines=[line.strip() for line in sys.stdin.readlines()]
for line in lines :
    is_or_not(line)