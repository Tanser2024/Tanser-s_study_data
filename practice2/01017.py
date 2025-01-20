while True:
    a1,a2,a3,a4,a5,a6=map(int,input().split())
    if a1+a2+a3+a4+a5+a6==0:
        break
    num=a6+a5+a4+(a3-1)//4+1
    if a3 %4==0:
        if a2>5*a4:
            num=num+(a2-5*a4-1)//9+1
    else:
        if a2>5*a4+(4-a3%4)*2-1:
            num=num+(a2 - 5 * a4 - (4 - a3 % 4) * 2 )//9+1
    if a1>36*(num-a6)-4*a2-9*a3-16*a4-25*a5:
        num=num+(a1-(36*(num-a6)-4*a2-9*a3-16*a4-25*a5)-1)//36+1
    print(num)









