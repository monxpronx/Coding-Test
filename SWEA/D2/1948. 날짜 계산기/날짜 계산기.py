# 260515

T = int(input())

for i in range(1, T+1):

    m1, d1, m2, d2 = map(int, input().split())

    total1, total2 = 0, 0

    for m in range(1, m1):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            total1 += 31
        elif m in [4, 6, 9, 11]:
            total1 += 30
        else:
            total1 += 28
    total1 += d1

    for m in range(1, m2):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            total2 += 31
        elif m in [4, 6, 9, 11]:
            total2 += 30
        else:
            total2 += 28
    total2 += d2

    print("#{} {}".format(i, total2-total1+1))