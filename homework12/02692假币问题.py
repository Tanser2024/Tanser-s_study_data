"""
t=int(input())
for _ in range(t):
    possible_light_coins=set()
    possible_heavy_coins=set()
    true_coins=set()
    for _ in range(3):
        data=list(input().split())
        if data[2]=="even":
            for i in range(2):
                true_coins|=set(data[i])
        else:
            if data[2]=="up":
                data[0],data[1]=data[1],data[0]
            possible_heavy_coins|=set(data[1])
            possible_light_coins|=set(data[0])
    true_coins|=(possible_heavy_coins&possible_heavy_coins)
    result_heavy=[x for x in possible_heavy_coins if x not in true_coins]
    result_light=[x for x in possible_light_coins if x not in true_coins]
    if result_heavy:
        print(f"{result_heavy[0]} is the counterfeit coin and it is heavy.")

    if result_light:
        print(f"{result_light[0]} is the counterfeit coin and it is light.")



"""
t = int(input())
for _ in range(t):
    fake_coins_heavy = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"}
    fake_coins_light = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"}
    data = []
    for _ in range(3):
        data.append(input().split())
    for left, right, result in data:
        if result == "even":
            fake_coins_heavy -= set(left + right)
            fake_coins_light -= set(left + right)
        elif result == "up":
            fake_coins_heavy &= set(left)
            fake_coins_light &= set(right)
        elif result == "down":
            fake_coins_heavy &= set(right)
            fake_coins_light &= set(left)

    heavy = list(fake_coins_heavy - fake_coins_light)
    light = list(fake_coins_light - fake_coins_heavy)

    if len(heavy) == 1:
        print(f"{heavy[0]} is the counterfeit coin and it is heavy.")
    elif len(light) == 1:
        print(f"{light[0]} is the counterfeit coin and it is light.")
