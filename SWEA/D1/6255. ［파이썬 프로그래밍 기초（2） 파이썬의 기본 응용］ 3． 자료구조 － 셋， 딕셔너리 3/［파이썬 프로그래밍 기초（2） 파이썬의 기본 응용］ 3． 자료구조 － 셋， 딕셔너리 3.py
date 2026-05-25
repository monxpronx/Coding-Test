# 260525

items = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000
    }


while 1:

    prices = []
    for key in items:
        prices.append(items[key])
    max_price = max(prices)

    if max_price == 0:
        break

    for key in items:
        if items[key] == max_price:
            print(key + ':', items[key])
            items[key] = 0