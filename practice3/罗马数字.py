w = str(input())
def luo_to_num(n):
    n=list(n)
    a = n.count("M")
    b = n.count("D")
    c = n.count("C")
    d = n.count("L")
    e = n.count("X")
    f = n.count("V")
    g = n.count("I")
    num = a*1000+b*500+c*100+d*50+e*10+f*5+g
    lst1= [n[i]+n[i+1] for i in range(len(n)-1)]
    num = num-lst1.count("IV")*2-lst1.count("IX")*2-lst1.count("XL")*20-lst1.count("XC")*20-lst1.count("CD")*200-lst1.count("CM")*200
    print(num)
def num_to_luo(n):
    n=int(n)
    rest1=n//1000
    rest2=n//100%10
    rest3=n//10%10
    rest4=n%10
    num="M"*rest1
    if rest2==4:
        num=num+"CD"
    elif rest2==9:
        num=num+"CM"
    elif rest2 in {1,2,3}:
        num=num+"C"*rest2
    elif rest2==5:
        num=num+"D"
    elif rest2!=0:
        num=num+"D"+"C"*(rest2-5)
    if rest3==4:
        num=num+"XL"
    elif rest3==9:
        num=num+"XC"
    elif rest3 in {1,2,3}:
        num=num+"X"*rest3
    elif rest3==5:
        num=num+"L"
    elif rest3 != 0:
        num=num+"L"+"X"*(rest3-5)
    if rest4==4:
        num=num+"IV"
    elif rest4==9:
        num=num+"IX"
    elif rest4 in {1,2,3}:
        num=num+"I"*rest4
    elif rest4==5:
        num=num+"V"
    elif rest4 != 0:
        num=num+"V"+"I"*(rest4-5)
    print(num)
if w[0] in {"1","2","3","4","5","6","7","8","9"}:
    num_to_luo(w)
else:
    luo_to_num(w)