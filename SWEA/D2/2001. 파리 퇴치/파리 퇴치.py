# 260517

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    max_num = 0
    for m1 in range(N-M+1):
        for m2 in range(N-M+1):
            num = 0
            for i in range(m1, m1+M):
                for j in range(m2, m2+M):
                    num += arr[i][j]
            if num > max_num:
                max_num = num

    print("#{} {}".format(t, max_num))
