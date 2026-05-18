# 260518

T = int(input())

for t in range(1, T+1):

    str1 = input()
    str2 = input()

    set_str1 = set(str1)

    max_cnt = 0
    for ch1 in set_str1:
        cnt = 0
        for ch2 in str2:
            if ch1 == ch2:
                cnt+=1
        if max_cnt < cnt:
            max_cnt = cnt

    print("#{} {}".format(t, max_cnt))