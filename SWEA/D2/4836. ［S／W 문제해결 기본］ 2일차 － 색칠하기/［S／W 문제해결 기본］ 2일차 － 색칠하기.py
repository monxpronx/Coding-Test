# 260520

T = int(input())

for t in range(1, T+1):

    # 2차원 0행렬 생성
    matrix = [[0]*10 for _ in range(10)]

    N = int(input())

    for n in range(N):

        x1, y1, x2, y2, c = map(int, input().split())

        # 빨간색 영역 칠하기
        if c == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    matrix[i][j] += 1

        # 파란색 영역 칠하기
        elif c == 2:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    matrix[i][j] += 2

        # 보라색 영역 확인
        cnt = 0
        for i in range(10):
            for j in range(10):
                if matrix[i][j] == 3:
                    cnt += 1

    print("#{} {}".format(t, cnt))