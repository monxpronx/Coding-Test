# 260514

T = int(input())

for i in range(1, T+1):

    string = input()

    for len in range(1, 10+1):
        
        token = string[:len]

        front_str = string[:30-30%len]
        back_str = string[30-30%len:]

        if front_str == token * (30//len) and back_str == token[:30%len]:
            break

    print("#{} {}".format(i, len))
