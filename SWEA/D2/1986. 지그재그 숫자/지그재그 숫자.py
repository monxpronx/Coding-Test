# 260514

T = int(input())

for i in range(1, T+1):

    n = int(input())

    total = 0
    for num in range(1, n+1):
        if num%2==1:
            total += num
        else:
            total -= num

    print("#{} {}".format(i, total))