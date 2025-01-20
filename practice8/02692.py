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
