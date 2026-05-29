# 260529

money = 0

for _ in range(3):
    ch, price = input().split()
    price = int(price)

    if ch == 'D':
        money += price
    else:
        money -= price

print("잔액: {}".format(money))