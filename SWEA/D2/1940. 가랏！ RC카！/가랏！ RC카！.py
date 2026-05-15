# 260515

T = int(input())

for t in range(1, T+1):

    n = int(input())
    v, distance = 0, 0

    for _ in range(n):

        command = list(map(int, input().split()))

        # command=1: 가속
        if command[0] == 1:
            v += command[1]
        # command=2: 감속
        elif command[0] == 2:
            if v < command[1]:
                v = 0
            else:
                v -= command[1]

        distance += v

    print("#{} {}".format(t, distance))