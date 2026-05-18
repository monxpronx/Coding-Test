# 260518

T = int(input())

for t in range(1, T+1):

    N, K = map(int, input().split())

    # 행렬 생성
    arr = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
    cnt = 0

    # 가로 검사
    for i in range(N):
        for j in range(N-K+1): ### j = 0,1,2
            sum_ij = 0
            for k in range(K): ### k = 0,1,2
                sum_ij += arr[i][j+k]
            if sum_ij == K:
                if (j == 0 or arr[i][j-1] == 0) and (j+k+1 == N or arr[i][j+k+1]==0):
                    cnt += 1

    # 세로 검사
    for j in range(N):
        for i in range(N-K+1):
            sum_ij = 0
            for k in range(K):
                sum_ij += arr[i+k][j]
            if sum_ij == K:
                if (i == 0 or arr[i-1][j] == 0) and (i+k+1 == N or arr[i+k+1][j]==0):
                    cnt += 1

    print("#{} {}".format(t, cnt))