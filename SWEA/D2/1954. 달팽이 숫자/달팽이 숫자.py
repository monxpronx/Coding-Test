# 260514

T = int(input())

for i in range(1, T+1):

    n = int(input())
    
    # nxn의 0행렬 생성
    matrix = [[0]*n for _ in range(n)]
    
    # 초기값 설정
    x, y = 0, 0
    d = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 시뮬레이션
    for num in range(1, n*n+1):

        matrix[x][y] = num

        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or n <= nx or ny < 0 or n <= ny or matrix[nx][ny]!=0:
            d = (d+1)%4
            nx = x + dx[d]
            ny = y + dy[d]
        x, y = nx, ny

    print("#{}".format(i))
    for j in range(n):
        print(*matrix[j])