# 260520

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    num_list = list(map(int, input().split()))

    max_total = float('-inf')
    min_total = float('inf')

    for i in range(N-M+1):

        total = sum(num_list[i:i+M])

        if total > max_total:
            max_total = total
        if total < min_total:
            min_total = total

    print("#{} {}".format(t, max_total-min_total))