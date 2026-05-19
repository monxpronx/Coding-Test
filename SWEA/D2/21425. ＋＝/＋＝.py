# 260519

T = int(input())

for t in range(1, T+1):

    A, B, N = map(int, input().split())

    tmp_min = min(A, B)
    tmp_max = max(A, B)
    cnt = 0

    while 1:

        min_num = min(tmp_min, tmp_max)
        max_num = max(tmp_min, tmp_max)

        min_num += max_num
        cnt += 1

        if min_num > N:
            break

        tmp_min = min_num
        tmp_max = max_num

    print(cnt)