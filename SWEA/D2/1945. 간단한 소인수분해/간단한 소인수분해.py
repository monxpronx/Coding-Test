# 260514

T = int(input())

for i in range(1, T+1):

    n = int(input())

    num = [2, 3, 5, 7, 11]
    cnt = [0, 0, 0, 0, 0]

    for j in range(4, -1, -1):
        while n % num[j] == 0:
            cnt[j] += 1
            n /= num[j]

    print("#{} {} {} {} {} {}".format(i, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4]))